import streamlit as st
import urllib.parse

# ==========================================
# PAGE CONFIG
# ==========================================
st.set_page_config(page_title="Zigcxy Bliss Store", layout="centered")

st.title("🕯️ Zigcxy Bliss - Candle Store")
st.write("Select your favorite candles ✨")

# ==========================================
# PRODUCT DATA (EDIT THIS)
# ==========================================

products = [
    {
        "name": "Asrtian Whimsy Button Jar.png",
        "price": 199,
        "stock": 6,
        "image": "images/Asrtian Whimsy Button Jar.png"
    },
    {
        "name": "Nature's Serenity Candle.png",
        "price": 199,
        "stock": 3,
        "image": "images/Nature's Serenity Candle.png"
    },
    {
        "name": "Coastal Mist Gel Jar",
        "price": 199,
        "stock": 5,
        "image": "images/Coastal Mist Gel Jar.png"
    },
    {
        "name": "Ocean Sunrise tall Shot Gel.png",
        "price": 299,
        "stock": 4,
        "image": "images/Ocean Sunrise tall Shot Gel.png"
    },
    {
        "name": "Sparkling Dessert Fizz Candle.png",
        "price": 399,
        "stock": 5,
        "image": "images/Sparkling Dessert Fizz Candle.png"
    }
]

# ==========================================
# CART
# ==========================================

cart = []

st.subheader("🛍️ Select Products")

for i, product in enumerate(products):

    st.image(product["image"], width=180)

    col1, col2 = st.columns([2, 1])

    with col1:
        st.write(f"**{product['name']}**")
        st.write(f"💰 ₹{product['price']}")
        st.write(f"📦 Available: {product['stock']}")

    with col2:
        qty = st.number_input(
            f"Qty {i}",
            min_value=0,
            max_value=product["stock"],
            step=1,
            key=f"qty_{i}"
        )

        if qty > 0:
            cart.append({
                "name": product["name"],
                "qty": qty,
                "price": product["price"],
                "total": qty * product["price"]
            })

    st.divider()

# ==========================================
# CART SUMMARY
# ==========================================

st.subheader("🧾 Order Summary")

total_amount = 0

if cart:
    for item in cart:
        st.write(f"{item['name']} x {item['qty']} = ₹{item['total']}")
        total_amount += item["total"]

    st.subheader(f"💰 Total: ₹{total_amount}")

else:
    st.info("No items selected")

# ==========================================
# CUSTOMER DETAILS
# ==========================================

st.subheader("📋 Customer Details")

name = st.text_input("Name")
mobile = st.text_input("Mobile Number")
hall = st.text_input("Hall No")
room = st.text_input("Room No")

# ==========================================
# WHATSAPP ORDER
# ==========================================

YOUR_NUMBER = "916394996857"  # change this

if st.button("Place Order on WhatsApp"):

    if not (name and mobile and cart):
        st.warning("⚠️ Fill details and select at least one item")

    else:
        order_text = "🕯️ *Zigcxy Bliss Order*\n\n"

        order_text += f"👤 Name: {name}\n"
        order_text += f"📱 Mobile: {mobile}\n"
        order_text += f"🏠 Hall: {hall}\n"
        order_text += f"🚪 Room: {room}\n\n"

        order_text += "🛍️ *Items Ordered:*\n"

        for item in cart:
            order_text += f"- {item['name']} x {item['qty']} = ₹{item['total']}\n"

        order_text += f"\n💰 *Total: ₹{total_amount}*"

        encoded = urllib.parse.quote(order_text)
        url = f"https://wa.me/{YOUR_NUMBER}?text={encoded}"

        st.link_button("📲 Always Confirm on WhatsApp", url)
        st.success("Click above button to confirm order ✅")
