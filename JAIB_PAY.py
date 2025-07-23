import streamlit as st

st.set_page_config(page_title="Jaib Pay", page_icon="🧾", layout="wide")

# --- Product data with placeholder image URLs (examples only) ---
products = {
    "ألعاب": {
        "PUBG": [
            {"name": "60 UC", "price": 3, "image": "https://static.pubg.com/images/uc_60.png"},
            {"name": "120 UC", "price": 5, "image": "https://static.pubg.com/images/uc_120.png"},
            {"name": "325 UC", "price": 10, "image": "https://static.pubg.com/images/uc_325.png"},
            {"name": "600 UC", "price": 18, "image": "https://static.pubg.com/images/uc_600.png"},
            {"name": "1300 UC", "price": 35, "image": "https://static.pubg.com/images/uc_1300.png"},
            {"name": "2700 UC", "price": 65, "image": "https://static.pubg.com/images/uc_2700.png"},
        ],
        "Free Fire": [
            {"name": "100 Diamonds", "price": 2, "image": "https://freefire.com/images/diamonds_100.png"},
            {"name": "310 Diamonds", "price": 6, "image": "https://freefire.com/images/diamonds_310.png"},
            {"name": "520 Diamonds", "price": 10, "image": "https://freefire.com/images/diamonds_520.png"},
            {"name": "1100 Diamonds", "price": 20, "image": "https://freefire.com/images/diamonds_1100.png"},
        ],
        "Call of Duty Mobile": [
            {"name": "80 CP", "price": 1, "image": "https://placehold.co/150x120/4A4A4A/FFFFFF?text=CoD+80CP"},
            {"name": "400 CP", "price": 5, "image": "https://placehold.co/150x120/4A4A4A/FFFFFF?text=CoD+400CP"},
            {"name": "800 CP", "price": 10, "image": "https://placehold.co/150x120/4A4A4A/FFFFFF?text=CoD+800CP"},
            {"name": "2000 CP", "price": 25, "image": "https://placehold.co/150x120/4A4A4A/FFFFFF?text=CoD+2000CP"},
        ],
        "Fortnite": [
            {"name": "1000 V-Bucks", "price": 8, "image": "https://placehold.co/150x120/7C4DFF/FFFFFF?text=Fortnite+V-Bucks"},
            {"name": "2800 V-Bucks", "price": 20, "image": "https://placehold.co/150x120/7C4DFF/FFFFFF?text=Fortnite+V-Bucks"},
            {"name": "5000 V-Bucks", "price": 35, "image": "https://placehold.co/150x120/7C4DFF/FFFFFF?text=Fortnite+V-Bucks"},
        ],
        "Valorant": [
            {"name": "400 VP", "price": 5, "image": "https://placehold.co/150x120/FF4655/FFFFFF?text=Valorant+VP"},
            {"name": "800 VP", "price": 10, "image": "https://placehold.co/150x120/FF4655/FFFFFF?text=Valorant+VP"},
            {"name": "1700 VP", "price": 20, "image": "https://placehold.co/150x120/FF4655/FFFFFF?text=Valorant+VP"},
        ],
        "Mobile Legends": [
            {"name": "100 Diamonds", "price": 2, "image": "https://placehold.co/150x120/007BFF/FFFFFF?text=MLBB+Diamonds"},
            {"name": "250 Diamonds", "price": 5, "image": "https://placehold.co/150x120/007BFF/FFFFFF?text=MLBB+Diamonds"},
            {"name": "500 Diamonds", "price": 10, "image": "https://placehold.co/150x120/007BFF/FFFFFF?text=MLBB+Diamonds"},
        ],
    },
    "برامج": {
        "Microsoft Office": [
            {"name": "اشتراك سنوي", "price": 30, "image": "https://placehold.co/150x120/D32F2F/FFFFFF?text=MS+Office+Annual"},
            {"name": "مدى الحياة", "price": 80, "image": "https://placehold.co/150x120/D32F2F/FFFFFF?text=MS+Office+Lifetime"},
        ],
        "VPN": [
            {"name": "شهر واحد", "price": 4, "image": "https://placehold.co/150x120/2196F3/FFFFFF?text=VPN+1+Month"},
            {"name": "سنة", "price": 35, "image": "https://placehold.co/150x120/2196F3/FFFFFF?text=VPN+1+Year"},
        ],
    },
    "بطائق الكترونية": {
        "بطاقات هدايا": [
            {"name": "بطاقة iTunes 10$", "price": 10, "image": "https://placehold.co/150x120/9C27B0/FFFFFF?text=iTunes+10$"},
            {"name": "بطاقة Google Play 25$", "price": 25, "image": "https://placehold.co/150x120/4CAF50/FFFFFF?text=Google+Play+25$"},
            {"name": "بطاقة PlayStation 50$", "price": 50, "image": "https://placehold.co/150x120/0070D1/FFFFFF?text=PSN+50$"},
            {"name": "بطاقة Xbox 20$", "price": 20, "image": "https://placehold.co/150x120/107C10/FFFFFF?text=Xbox+20$"},
        ],
        "بطاقات شحن": [
            {"name": "رصيد موبايل 5$", "price": 5, "image": "https://placehold.co/150x120/FFC107/333333?text=Mobile+Recharge+5$"},
            {"name": "رصيد موبايل 10$", "price": 10, "image": "https://placehold.co/150x120/FFC107/333333?text=Mobile+Recharge+10$"},
            {"name": "رصيد موبايل 20$", "price": 20, "image": "https://placehold.co/150x120/FFC107/333333?text=Mobile+Recharge+20$"},
        ],
    },
    "إشتراكات": {
        "خدمات بث": [
            {"name": "اشتراك Netflix شهر", "price": 15, "image": "https://placehold.co/150x120/E50914/FFFFFF?text=Netflix+1+Month"},
            {"name": "اشتراك Spotify سنة", "price": 100, "image": "https://placehold.co/150x120/1DB954/FFFFFF?text=Spotify+1+Year"},
            {"name": "اشتراك YouTube Premium 3 أشهر", "price": 30, "image": "https://placehold.co/150x120/FF0000/FFFFFF?text=YouTube+3+Months"},
        ],
        "ألعاب": [
            {"name": "اشتراك PlayStation Plus 3 أشهر", "price": 25, "image": "https://placehold.co/150x120/003791/FFFFFF?text=PS+Plus+3M"},
            {"name": "اشتراك Xbox Game Pass شهر", "price": 10, "image": "https://placehold.co/150x120/107C10/FFFFFF?text=Xbox+Game+Pass+1M"},
            {"name": "اشتراك Nintendo Switch Online سنة", "price": 20, "image": "https://placehold.co/150x120/E60012/FFFFFF?text=Nintendo+Online+1Y"},
        ],
        "برامج تصميم": [
            {"name": "اشتراك Adobe Creative Cloud شهر", "price": 50, "image": "https://placehold.co/150x120/DA1F26/FFFFFF?text=Adobe+CC+1M"},
            {"name": "اشتراك Canva Pro سنة", "price": 120, "image": "https://placehold.co/150x120/00C4CC/FFFFFF?text=Canva+Pro+1Y"},
        ],
    },
}

categories = list(products.keys())

# Initialize session state if not already present
if 'selected_category' not in st.session_state:
    st.session_state['selected_category'] = categories[0]
if 'selected_service' not in st.session_state:
    st.session_state['selected_service'] = None
if 'selected_package' not in st.session_state:
    st.session_state['selected_package'] = None
if 'payment_message_type' not in st.session_state:
    st.session_state['payment_message_type'] = ''
if 'payment_message_text' not in st.session_state:
    st.session_state['payment_message_text'] = ''
if 'language' not in st.session_state:
    st.session_state['language'] = 'ar' # Default language is Arabic
if 'search_query' not in st.session_state:
    st.session_state['search_query'] = ''


# Language data
lang_data = {
    'ar': {
        'app_title': "Jaib Pay 🧾",
        'choose_category': "اختر الفئة",
        'choose_service': "اختر الخدمة",
        'available_packages_for': "الباقات المتاحة لـ",
        'buy': "شراء",
        'choose_payment_method': "💳 اختر طريقة الدفع",
        'purchase_code': "كود الشراء",
        'visa_card': "بطاقة فيزا",
        'enter_purchase_code': "أدخل كود الشراء (يبدأ بـ JP)",
        'confirm_payment': "تأكيد الدفع",
        'purchase_success_code': "✅ تم شراء {package_name} بنجاح باستخدام كود الشراء",
        'invalid_code': "⚠️ كود غير صالح، تأكد من صحته",
        'visa_card_number': "رقم بطاقة الفيزا",
        'expiry_date': "تاريخ الانتهاء (MM/YY)",
        'cvv': "CVV",
        'confirm_visa_payment': "تأكيد الدفع عبر فيزا",
        'purchase_success_visa': "✅ تم شراء {package_name} بنجاح باستخدام بطاقة الفيزا",
        'invalid_card_data': "❌ بيانات البطاقة غير صحيحة",
        'select_category_info': "الرجاء اختيار فئة لعرض المنتجات.",
        'search_placeholder': "ابحث عن الألعاب أو البطاقات...",
        'login': "تسجيل الدخول",
        'cart': "🛒 سلة المشتريات",
        'language_label': "اللغة:",
        'arabic': "العربية",
        'english': "الإنجليزية"
    },
    'en': {
        'app_title': "Jaib Pay 🧾",
        'choose_category': "Choose Category",
        'choose_service': "Choose Service",
        'available_packages_for': "Available Packages for",
        'buy': "Buy",
        'choose_payment_method': "💳 Choose Payment Method",
        'purchase_code': "Purchase Code",
        'visa_card': "Visa Card",
        'enter_purchase_code': "Enter Purchase Code (starts with JP)",
        'confirm_payment': "Confirm Payment",
        'purchase_success_code': "✅ Successfully purchased {package_name} using purchase code",
        'invalid_code': "⚠️ Invalid code, please check it",
        'visa_card_number': "Visa Card Number",
        'expiry_date': "Expiry Date (MM/YY)",
        'cvv': "CVV",
        'confirm_visa_payment': "Confirm Payment via Visa",
        'purchase_success_visa': "✅ Successfully purchased {package_name} using Visa card",
        'invalid_card_data': "❌ Incorrect card data",
        'select_category_info': "Please select a category to view products.",
        'search_placeholder': "Search for games or cards...",
        'login': "Login",
        'cart': "🛒 Shopping Cart",
        'language_label': "Language:",
        'arabic': "Arabic",
        'english': "English"
    }
}

def _(key):
    """Helper function for translation."""
    return lang_data[st.session_state['language']].get(key, key)


# Function to get category icon (using emojis as a simple representation in Streamlit)
def get_category_icon(category_name):
    if category_name == "ألعاب":
        return "🎮"
    elif category_name == "برامج":
        return "📦"
    elif category_name == "بطائق الكترونية":
        return "🎁"
    elif category_name == "إشتراكات":
        return "🔄"
    else:
        return ""

# Custom CSS for overall styling
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

    html, body, [data-testid="stAppViewContainer"] {
        font-family: 'Inter', sans-serif;
        background-color: #f0f2f6; /* Light gray background for the whole page */
    }

    /* Main container styling */
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        padding-left: 1rem;
        padding-right: 1rem;
        max-width: 1200px; /* Limit content width */
    }

    /* Header container styling */
    .st-emotion-cache-1cypcdb { /* Target the Streamlit header container */
        background-color: #ffffff;
        padding: 1rem 2rem;
        border-bottom: 1px solid #e0e0e0;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
        border-radius: 0.75rem; /* rounded-xl */
        margin-bottom: 2rem;
    }

    /* Adjust Streamlit's default button styling for category buttons */
    .stButton > button {
        width: 100%;
        height: 100px;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        border-radius: 0.75rem; /* rounded-xl */
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06); /* shadow-md */
        transition: all 0.3s ease;
        font-size: 1.125rem; /* text-lg */
        font-weight: 500; /* font-medium */
        color: #4b5563; /* text-gray-700 */
        background-color: #f3f4f6; /* bg-gray-100 */
        border: none;
        cursor: pointer;
    }
    .stButton > button:hover {
        background-color: #e0f2fe; /* hover:bg-blue-100 */
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05); /* hover:shadow-lg */
        transform: scale(1.03); /* Slightly less aggressive hover */
    }
    .stButton > button:focus {
        outline: none;
        box-shadow: 0 0 0 4px rgba(96, 165, 250, 0.5); /* focus:ring-4 focus:ring-blue-300 */
    }

    /* Specific style for selected category button */
    .stButton > button[data-testid="stButton-primary"] {
        background-color: #2563eb; /* bg-blue-600 */
        color: white;
        transform: scale(1.05);
        box-shadow: 0 0 0 4px rgba(96, 165, 250, 0.5); /* ring-4 ring-blue-300 */
    }

    /* Product card styling */
    .product-card {
        background-color: white;
        border: 1px solid #e2e8f0; /* border-gray-200 */
        border-radius: 0.75rem; /* rounded-xl */
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06); /* shadow-md */
        overflow: hidden;
        padding: 1rem;
        display: flex;
        flex-direction: column;
        align-items: center;
        text-align: center;
        transition: all 0.3s ease;
        height: 100%; /* Ensure cards have consistent height */
    }
    .product-card:hover {
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05); /* hover:shadow-lg */
        transform: scale(1.03); /* Slightly less aggressive hover */
    }
    .product-image {
        width: 100%;
        height: 128px; /* h-32 */
        object-fit: contain;
        margin-bottom: 1rem;
        border-radius: 0.5rem; /* rounded-lg */
    }
    .product-name {
        font-size: 1.25rem; /* text-xl */
        font-weight: bold;
        margin-bottom: 0.5rem;
    }
    .product-price {
        color: #16a34a; /* text-green-600 */
        font-size: 1.5rem; /* text-2xl */
        font-weight: 800; /* font-extrabold */
        margin-bottom: 1rem;
    }
    .buy-button {
        width: 100%;
        background-color: #2563eb; /* bg-blue-600 */
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 0.5rem; /* rounded-lg */
        transition: all 0.3s ease;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06); /* shadow-lg */
        border: none;
        cursor: pointer;
        margin-top: auto; /* Push button to the bottom of the card */
    }
    .buy-button:hover {
        background-color: #1d4ed8; /* hover:bg-blue-700 */
    }
    .buy-button:focus {
        outline: none;
        box-shadow: 0 0 0 4px rgba(96, 165, 250, 0.5); /* focus:ring-4 focus:ring-blue-300 */
    }

    /* Streamlit input fields and select boxes */
    .stTextInput > div > div > input, .stSelectbox > div > div {
        border-radius: 0.5rem;
        border: 1px solid #d1d5db; /* gray-300 */
        padding: 0.5rem 0.75rem;
        box-shadow: inset 0 1px 2px rgba(0,0,0,0.05);
    }
    .stTextInput > div > div > input:focus, .stSelectbox > div > div:focus-within {
        border-color: #3b82f6; /* blue-500 */
        box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.25); /* ring-blue-500 */
    }

    /* Payment radio buttons */
    .stRadio > label {
        font-weight: 600; /* semibold */
        color: #333;
    }
    .stRadio > div {
        justify-content: center; /* Center radio buttons */
        gap: 2rem; /* Space between radio options */
    }
    .stRadio > div > label {
        background-color: #f3f4f6; /* bg-gray-100 */
        padding: 0.75rem 1.5rem;
        border-radius: 0.5rem;
        border: 1px solid #e2e8f0;
        transition: all 0.2s ease;
        cursor: pointer;
    }
    .stRadio > div > label:hover {
        background-color: #e0f2fe;
        border-color: #93c5fd; /* blue-300 */
    }
    .stRadio > div > label[data-baseweb="radio"] { /* Target selected radio button */
        background-color: #2563eb;
        color: white;
        border-color: #2563eb;
    }
    .stRadio > div > label[data-baseweb="radio"] > div > div {
        border-color: white !important; /* Checkmark color */
    }

    /* Message boxes */
    .stAlert {
        border-radius: 0.75rem;
        padding: 1rem 1.5rem;
        font-weight: 500;
        text-align: center;
    }

    /* Adjust Streamlit's default padding for columns to reduce unnecessary space */
    .st-emotion-cache-1r6slb0 { /* Target column padding */
        padding-left: 0.5rem;
        padding-right: 0.5rem;
    }
    </style>
""", unsafe_allow_html=True)


# --- Header Section: Search, Language, Login, Cart ---
# Use a container for the header to apply consistent styling
with st.container():
    header_cols = st.columns([0.8, 2, 0.5, 0.5]) # Adjust column ratios as needed

    with header_cols[0]:
        # Language selection
        st.markdown(f"<div style='direction: {'rtl' if st.session_state['language'] == 'ar' else 'ltr'};'>", unsafe_allow_html=True)
        lang_choice = st.radio(
            _('language_label'),
            [_('arabic'), _('english')],
            key="language_selector",
            horizontal=True,
            index=0 if st.session_state['language'] == 'ar' else 1,
            label_visibility="collapsed"
        )
        st.markdown("</div>", unsafe_allow_html=True)
        if lang_choice == _('arabic') and st.session_state['language'] != 'ar':
            st.session_state['language'] = 'ar'
            st.rerun()
        elif lang_choice == _('english') and st.session_state['language'] != 'en':
            st.session_state['language'] = 'en'
            st.rerun()

    with header_cols[1]:
        # Search bar
        st.session_state['search_query'] = st.text_input(
            "",
            placeholder=_('search_placeholder'),
            key="search_bar_input",
            label_visibility="collapsed"
        )

    with header_cols[2]:
        # Login button
        st.markdown(f"""
            <button class="buy-button" style="width:100%; background-color:#6b7280; margin-bottom:0; height:40px; font-size:1rem; box-shadow:none;" onclick="alert('{_('login')} functionality not implemented yet.')">
                {_('login')}
            </button>
        """, unsafe_allow_html=True)
        # Note: Streamlit buttons cannot directly trigger JS alerts. Using a workaround.
        # For a real app, this would trigger a Streamlit modal or state change.

    with header_cols[3]:
        # Cart button
        st.markdown(f"""
            <button class="buy-button" style="width:100%; background-color:#6b7280; margin-bottom:0; height:40px; font-size:1rem; box-shadow:none;" onclick="alert('{_('cart')} functionality not implemented yet.')">
                {_('cart')}
            </button>
        """, unsafe_allow_html=True)
        # Similar workaround for cart button.

st.markdown(f"<h1 style='text-align:center; color:#1e40af; margin-top:2rem;'>{_('app_title')}</h1>", unsafe_allow_html=True)

# --- Category Selection ---
st.markdown(f"<h2 style='text-align:center; color:#333; margin-top:2rem;'>{_('choose_category')}</h2>", unsafe_allow_html=True)

cols = st.columns(len(categories))
for i, cat in enumerate(categories):
    with cols[i]:
        # Streamlit button for category selection, styled by CSS
        if st.session_state['selected_category'] == cat:
            if st.button(f"{get_category_icon(cat)} {cat}", key=f"cat_btn_{cat}", type="primary"):
                st.session_state['selected_category'] = cat
                st.session_state['selected_service'] = list(products[cat].keys())[0] if products[cat] else None
                st.session_state['selected_package'] = None
                st.session_state['payment_message_type'] = ''
                st.session_state['payment_message_text'] = ''
                st.rerun() # Rerun to update the service dropdown immediately
        else:
            if st.button(f"{get_category_icon(cat)} {cat}", key=f"cat_btn_{cat}"):
                st.session_state['selected_category'] = cat
                st.session_state['selected_service'] = list(products[cat].keys())[0] if products[cat] else None
                st.session_state['selected_package'] = None
                st.session_state['payment_message_type'] = ''
                st.session_state['payment_message_text'] = ''
                st.rerun() # Rerun to update the service dropdown immediately

category = st.session_state['selected_category']

# --- Service Selection within the Category ---
if category:
    services = list(products[category].keys())
    
    # Set default service if selected_service is not valid for the current category
    if st.session_state['selected_service'] not in services:
        st.session_state['selected_service'] = services[0] if services else None

    service = st.selectbox(
        _('choose_service'),
        services,
        index=services.index(st.session_state['selected_service']) if st.session_state['selected_service'] in services else 0,
        key="service_select_box"
    )
    st.session_state['selected_service'] = service

    st.markdown(f"<h3 style='text-align:center; color:#333; margin-top:2rem;'>{_('available_packages_for')} {service}</h3>", unsafe_allow_html=True)

    items = products[category][service]

    # Filter items based on search query
    search_query_lower = st.session_state['search_query'].lower()
    if search_query_lower:
        items = [item for item in items if search_query_lower in item['name'].lower()]
    
    if not items:
        st.info("No products found matching your search criteria.")

    # --- Display 4-column grid ---
    num_cols = 4
    cols = st.columns(num_cols)

    for idx, item in enumerate(items):
        with cols[idx % num_cols]:
            # Using custom HTML for the product card for better styling control
            st.markdown(f"""
                <div class="product-card">
                    <img src="{item['image']}" alt="{item['name']}" class="product-image" onerror="this.onerror=null; this.src='https://placehold.co/150x120/E0E0E0/333333?text={item['name'].replace(' ', '+')}';">
                    <div class="product-name">{item['name']}</div>
                    <div class="product-price">{item['price']}$</div>
                    <button class="buy-button" key="buy_btn_{item['name']}_{idx}" onclick="window.parent.postMessage({{streamlit: {{type: 'SET_SESSION_STATE', args: ['selected_package', {item!r}]}}}}, '*')">
                        {_('buy')}
                    </button>
                </div>
            """, unsafe_allow_html=True)
            # Streamlit buttons below custom HTML for proper state management
            # This hidden button will be triggered by the custom HTML button's JS
            if st.button(_('buy'), key=f"buy_hidden_{item['name']}_{idx}", help="Hidden button for state management", disabled=True):
                # This block will not be directly executed by user clicks on the custom HTML button
                # It's here for Streamlit's internal state management and to ensure the key is unique
                pass

# --- Payment Options ---
if st.session_state['selected_package']:
    st.markdown("---")
    st.markdown(f"<h3 style='text-align:center; color:#333;'>{_('choose_payment_method')}</h3>", unsafe_allow_html=True)

    pay_option = st.radio(
        _('choose_payment_method'),
        (_('purchase_code'), _('visa_card')),
        key="payment_method_radio",
        horizontal=True,
        label_visibility="collapsed"
    )

    # Use a container for the payment form for better visual grouping
    with st.container():
        st.markdown("""
            <style>
            .payment-form-container {
                background-color: #ffffff;
                padding: 2rem;
                border-radius: 0.75rem;
                box-shadow: 0 4px 12px rgba(0,0,0,0.08);
                max-width: 600px;
                margin: 2rem auto; /* Center the form */
            }
            </style>
            <div class="payment-form-container">
        """, unsafe_allow_html=True)

        if pay_option == _('purchase_code'):
            code = st.text_input(_('enter_purchase_code'), key="purchase_code_input")

            if st.button(_('confirm_payment'), key="confirm_code_payment_btn"):
                if code.startswith("JP") and len(code) == 10:
                    st.session_state['payment_message_type'] = 'success'
                    st.session_state['payment_message_text'] = _('purchase_success_code').format(package_name=st.session_state['selected_package']['name'])
                else:
                    st.session_state['payment_message_type'] = 'warning'
                    st.session_state['payment_message_text'] = _('invalid_code')
                st.rerun() # Rerun to display message

        elif pay_option == _('visa_card'):
            card_number = st.text_input(_('visa_card_number'), key="card_number_input")
            col1, col2 = st.columns(2)
            with col1:
                expiry_date = st.text_input(_('expiry_date'), key="expiry_date_input")
            with col2:
                cvv = st.text_input(_('cvv'), type="password", key="cvv_input")

            if st.button(_('confirm_visa_payment'), key="confirm_visa_payment_btn"):
                # In a real application, card validation and payment gateway integration would happen here
                if len(card_number) == 16 and len(expiry_date) == 5 and len(cvv) == 3:
                    st.session_state['payment_message_type'] = 'success'
                    st.session_state['payment_message_text'] = _('purchase_success_visa').format(package_name=st.session_state['selected_package']['name'])
                else:
                    st.session_state['payment_message_type'] = 'error'
                    st.session_state['payment_message_text'] = _('invalid_card_data')
                st.rerun() # Rerun to display message
        
        st.markdown("</div>", unsafe_allow_html=True) # Close payment-form-container

# Display payment message
if st.session_state['payment_message_text']:
    if st.session_state['payment_message_type'] == 'success':
        st.success(st.session_state['payment_message_text'])
    elif st.session_state['payment_message_type'] == 'warning':
        st.warning(st.session_state['payment_message_text'])
    elif st.session_state['payment_message_type'] == 'error':
        st.error(st.session_state['payment_message_text'])
