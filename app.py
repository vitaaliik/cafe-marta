import os
import shutil
import uuid

from fastapi import FastAPI, Request, Form, Query, UploadFile, File
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.middleware.sessions import SessionMiddleware

from database import Base, engine, SessionLocal
from models import Product

app = FastAPI()

app.add_middleware(SessionMiddleware, secret_key="marta_super_secret_key")

Base.metadata.create_all(bind=engine)

app.mount("/static", StaticFiles(directory="static"), name="static")
app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")

templates = Jinja2Templates(directory="templates")

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


@app.get("/")
def index(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )


@app.get("/menu", response_class=HTMLResponse)
def menu(request: Request):
    db = SessionLocal()
    products = db.query(Product).all()
    db.close()

    grouped_menu = {}

    for product in products:
        category = product.category or "Інше"
        subcategory = product.subcategory or "Без підкатегорії"

        if category not in grouped_menu:
            grouped_menu[category] = {}

        if subcategory not in grouped_menu[category]:
            grouped_menu[category][subcategory] = []

        grouped_menu[category][subcategory].append(product)

    return templates.TemplateResponse(
        request=request,
        name="menu.html",
        context={"grouped_menu": grouped_menu}
    )


@app.get("/contacts", response_class=HTMLResponse)
def contacts(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="contacts.html"
    )


@app.get("/login", response_class=HTMLResponse)
def login_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="login.html",
        context={"error": ""}
    )


@app.post("/login", response_class=HTMLResponse)
def login(request: Request, username: str = Form(...), password: str = Form(...)):
    if username == "admin" and password == "1234":
        request.session["admin"] = True
        return RedirectResponse(url="/admin", status_code=303)

    return templates.TemplateResponse(
        request=request,
        name="login.html",
        context={"error": "Неправильний логін або пароль"}
    )


@app.get("/logout")
def logout(request: Request):
    request.session.clear()
    return RedirectResponse(url="/login", status_code=303)


@app.get("/admin", response_class=HTMLResponse)
def admin_page(request: Request, search: str = Query(default="")):
    if not request.session.get("admin"):
        return RedirectResponse(url="/login", status_code=303)

    db = SessionLocal()
    query = db.query(Product)

    if search:
        query = query.filter(Product.name.ilike(f"%{search}%"))

    products = query.all()
    db.close()

    return templates.TemplateResponse(
        request=request,
        name="admin.html",
        context={
            "products": products,
            "search": search
        }
    )


@app.post("/admin/add-product")
def add_product(
    request: Request,
    name: str = Form(...),
    description: str = Form(""),
    weight: str = Form(""),
    price: float = Form(...),
    category: str = Form(...),
    subcategory: str = Form(""),
    image: UploadFile | None = File(None)
):
    if not request.session.get("admin"):
        return RedirectResponse(url="/login", status_code=303)

    image_filename = None

    if image and image.filename:
        ext = os.path.splitext(image.filename)[1]
        image_filename = f"{uuid.uuid4().hex}{ext}"
        image_path = os.path.join(UPLOAD_DIR, image_filename)

        with open(image_path, "wb") as buffer:
            shutil.copyfileobj(image.file, buffer)

    db = SessionLocal()

    new_product = Product(
        name=name,
        description=description,
        weight=weight,
        price=price,
        category=category,
        subcategory=subcategory,
        image_filename=image_filename
    )

    db.add(new_product)
    db.commit()
    db.close()

    return RedirectResponse(url="/admin", status_code=303)


@app.get("/admin/delete/{product_id}")
def delete_product(product_id: int, request: Request):
    if not request.session.get("admin"):
        return RedirectResponse(url="/login", status_code=303)

    db = SessionLocal()
    product = db.query(Product).filter(Product.id == product_id).first()

    if product:
        if product.image_filename:
            image_path = os.path.join(UPLOAD_DIR, product.image_filename)
            if os.path.exists(image_path):
                os.remove(image_path)

        db.delete(product)
        db.commit()

    db.close()

    return RedirectResponse(url="/admin", status_code=303)


@app.get("/admin/edit/{product_id}", response_class=HTMLResponse)
def edit_product_page(product_id: int, request: Request):
    if not request.session.get("admin"):
        return RedirectResponse(url="/login", status_code=303)

    db = SessionLocal()
    product = db.query(Product).filter(Product.id == product_id).first()
    db.close()

    if not product:
        return RedirectResponse(url="/admin", status_code=303)

    return templates.TemplateResponse(
        request=request,
        name="edit_product.html",
        context={"product": product}
    )

@app.get("/admin/delete-photo/{product_id}")
def delete_product_photo(product_id: int, request: Request):
    if not request.session.get("admin"):
        return RedirectResponse(url="/login", status_code=303)

    db = SessionLocal()
    product = db.query(Product).filter(Product.id == product_id).first()

    if product and product.image_filename:
        image_path = os.path.join(UPLOAD_DIR, product.image_filename)

        if os.path.exists(image_path):
            os.remove(image_path)

        product.image_filename = None
        db.commit()

    db.close()

    return RedirectResponse(url=f"/admin/edit/{product_id}", status_code=303)

@app.post("/admin/edit/{product_id}")
def edit_product(
    product_id: int,
    request: Request,
    name: str = Form(...),
    description: str = Form(""),
    weight: str = Form(""),
    price: float = Form(...),
    category: str = Form(...),
    subcategory: str = Form(""),
    image: UploadFile | None = File(None)
):
    if not request.session.get("admin"):
        return RedirectResponse(url="/login", status_code=303)

    db = SessionLocal()
    product = db.query(Product).filter(Product.id == product_id).first()

    if product:
        product.name = name
        product.description = description
        product.weight = weight
        product.price = price
        product.category = category
        product.subcategory = subcategory

        if image and image.filename:
            if product.image_filename:
                old_image_path = os.path.join(UPLOAD_DIR, product.image_filename)
                if os.path.exists(old_image_path):
                    os.remove(old_image_path)

            ext = os.path.splitext(image.filename)[1]
            image_filename = f"{uuid.uuid4().hex}{ext}"
            image_path = os.path.join(UPLOAD_DIR, image_filename)

            with open(image_path, "wb") as buffer:
                shutil.copyfileobj(image.file, buffer)

            product.image_filename = image_filename

        db.commit()

    db.close()

    return RedirectResponse(url="/admin", status_code=303)


@app.get("/ping")
def ping():
    return {"status": "ok"}