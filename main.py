import streamlit as st
from services.sweet_service import SweetService
from models.sweet import Sweet

# Initialize the service
if 'service' not in st.session_state:
    st.session_state.service = SweetService()

service = st.session_state.service

# Custom CSS for modern, minimalistic design
st.markdown("""
<style>
    .main-header {
        text-align: center;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 3rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }
    
    .subtitle {
        text-align: center;
        color: #6c757d;
        font-size: 1.1rem;
        margin-bottom: 2rem;
        font-weight: 300;
    }
    
    .section-header {
        font-size: 1.5rem;
        font-weight: 600;
        color: #495057;
        margin: 2rem 0 1rem 0;
        padding-bottom: 0.5rem;
        border-bottom: 2px solid #e9ecef;
    }
    
    .metric-container {
        background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
        border-radius: 15px;
        padding: 1.5rem;
        margin: 1rem 0;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        border: 1px solid #dee2e6;
    }
    
    .sweet-card {
        background: white;
        border-radius: 12px;
        padding: 1.5rem;
        margin: 0.5rem 0;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
        border-left: 4px solid #667eea;
        transition: transform 0.2s ease;
    }
    
    .sweet-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
    }
    
    .sweet-name {
        font-size: 1.2rem;
        font-weight: 600;
        color: #343a40;
        margin-bottom: 0.5rem;
    }
    
    .sweet-details {
        color: #6c757d;
        font-size: 0.9rem;
        margin-bottom: 0.3rem;
    }
    
    .price-tag {
        background: linear-gradient(135deg, #28a745, #20c997);
        color: white;
        padding: 0.3rem 0.8rem;
        border-radius: 20px;
        font-weight: 600;
        font-size: 0.9rem;
        display: inline-block;
        margin-top: 0.5rem;
    }
    
    .empty-state {
        text-align: center;
        color: #6c757d;
        background: #f8f9fa;
        padding: 3rem;
        border-radius: 15px;
        margin: 2rem 0;
        border: 2px dashed #dee2e6;
    }
    
    .empty-state-icon {
        font-size: 3rem;
        margin-bottom: 1rem;
        opacity: 0.5;
    }
    
    .stats-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 1rem;
        margin: 1rem 0;
    }
    
    .stat-card {
        background: white;
        border-radius: 10px;
        padding: 1.5rem;
        text-align: center;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        border: 1px solid #e9ecef;
    }
    
    .stat-number {
        font-size: 2rem;
        font-weight: 700;
        color: #667eea;
        margin-bottom: 0.5rem;
    }
    
    .stat-label {
        color: #6c757d;
        font-size: 0.9rem;
        font-weight: 500;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    
    .form-section {
        background: white;
        border-radius: 15px;
        padding: 2rem;
        margin: 1rem 0;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
        border: 1px solid #e9ecef;
    }
    
    .delete-section {
        background: #fff5f5;
        border: 1px solid #fed7d7;
        border-radius: 15px;
        padding: 2rem;
        margin: 1rem 0;
    }
    
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 0.5rem 2rem;
        font-weight: 600;
        transition: all 0.3s ease;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }
    
    .stButton > button:hover {
        transform: translateY(-1px);
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15);
    }
    
    .delete-button > button {
        background: linear-gradient(135deg, #dc3545 0%, #c82333 100%);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 0.5rem 2rem;
        font-weight: 600;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown('<h1 class="main-header">🍭 Sweet Shop</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Minimal • Modern • Sweet Management</p>', unsafe_allow_html=True)

# Statistics Dashboard
sweets = service.get_all_sweets()
total_sweets = len(sweets)
total_quantity = sum(s.quantity for s in sweets)
categories = len(set(s.category for s in sweets)) if sweets else 0
avg_price = sum(s.price for s in sweets) / len(sweets) if sweets else 0

st.markdown('<div class="stats-grid">', unsafe_allow_html=True)
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(f'''
    <div class="stat-card">
        <div class="stat-number">{total_sweets}</div>
        <div class="stat-label">Total Sweets</div>
    </div>
    ''', unsafe_allow_html=True)

with col2:
    st.markdown(f'''
    <div class="stat-card">
        <div class="stat-number">{total_quantity}</div>
        <div class="stat-label">Total Stock</div>
    </div>
    ''', unsafe_allow_html=True)

with col3:
    st.markdown(f'''
    <div class="stat-card">
        <div class="stat-number">{categories}</div>
        <div class="stat-label">Categories</div>
    </div>
    ''', unsafe_allow_html=True)

with col4:
    st.markdown(f'''
    <div class="stat-card">
        <div class="stat-number">₹{avg_price:.0f}</div>
        <div class="stat-label">Avg Price</div>
    </div>
    ''', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# Tabs for better organization
tab1, tab2, tab3 = st.tabs(["➕ Add Sweet", "📋 View Sweets", "❌ Delete Sweet"])

with tab1:
    # st.markdown('<div class="form-section">', unsafe_allow_html=True)
    
    with st.form("add_form", clear_on_submit=True):
        col1, col2 = st.columns(2)
        
        with col1:
            id = st.number_input("Sweet ID", min_value=1000, step=1, help="Unique identifier for your sweet")
            name = st.text_input("Sweet Name", placeholder="e.g., Chocolate Truffle")
            category = st.text_input("Category", placeholder="e.g., Chocolate, Gummy, Hard Candy")
        
        with col2:
            price = st.number_input("Price (₹)", min_value=0.0, step=1.0, help="Price per unit")
            quantity = st.number_input("Quantity", min_value=1, step=1, help="Number of units in stock")
            st.write("")  # Spacer
            st.write("")  # Spacer

        submitted = st.form_submit_button("✨ Add Sweet", use_container_width=True)
        
        if submitted:
            if not name or not category:
                st.error("🚫 Please fill in all fields")
            else:
                try:
                    sweet = Sweet(id, name, category, price, quantity)
                    service.add_sweet(sweet)
                    st.success(f"✅ {name} added successfully!")
                    st.balloons()
                    st.rerun()
                except ValueError as e:
                    st.error(f"🚫 {str(e)}")
    
    st.markdown('</div>', unsafe_allow_html=True)

with tab2:
    if sweets:
        # Search and filter
        col1, col2 = st.columns([3, 1])
        with col1:
            search_term = st.text_input("🔍 Search sweets...", placeholder="Search by name or category")
        with col2:
            sort_by = st.selectbox("Sort by", ["Name", "Price", "Quantity", "Category"])
        
        # Filter sweets based on search
        filtered_sweets = sweets
        if search_term:
            filtered_sweets = [s for s in sweets if 
                             search_term.lower() in s.name.lower() or 
                             search_term.lower() in s.category.lower()]
        
        # Sort sweets using service methods
        if sort_by == "Name":
            all_sorted = service.sort_by_name()
        elif sort_by == "Price":
            all_sorted = service.sort_by_price(descending=True)
        elif sort_by == "Quantity":
            all_sorted = service.sort_by_quantity(descending=True)
        elif sort_by == "Category":
            all_sorted = sorted(service.get_all_sweets(), key=lambda x: x.category)
        
        # Apply search filter to sorted results
        if search_term:
            filtered_sweets = [s for s in all_sorted if 
                             search_term.lower() in s.name.lower() or 
                             search_term.lower() in s.category.lower()]
        else:
            filtered_sweets = all_sorted
        
        # Display sweets in cards
        for sweet in filtered_sweets:
            st.markdown(f'''
            <div class="sweet-card">
                <div class="sweet-name">{sweet.name}</div>
                <div class="sweet-details">
                    <strong>ID:</strong> {sweet.id} | 
                    <strong>Category:</strong> {sweet.category} | 
                    <strong>Stock:</strong> {sweet.quantity} units
                </div>
                <div class="price-tag">₹{sweet.price}</div>
            </div>
            ''', unsafe_allow_html=True)
        
        if not filtered_sweets and search_term:
            st.info(f"🔍 No sweets found matching '{search_term}'")
            
    else:
        st.markdown('''
        <div class="empty-state">
            <div class="empty-state-icon">🍭</div>
            <h3>No sweets available</h3>
            <p>Start by adding your first sweet to the inventory!</p>
        </div>
        ''', unsafe_allow_html=True)

with tab3:
    st.markdown('<div class="delete-section">', unsafe_allow_html=True)
    
    if sweets:
        col1, col2 = st.columns([2, 1])
        
        with col1:
            # Create a selectbox with sweet names and IDs
            sweet_options = {f"{s.name} (ID: {s.id})": s.id for s in sweets}
            selected_sweet = st.selectbox("Select sweet to delete", options=list(sweet_options.keys()))
            delete_id = sweet_options[selected_sweet] if selected_sweet else None
        
        with col2:
            st.write("")  # Spacer
            st.markdown('<div class="delete-button">', unsafe_allow_html=True)
            if st.button("🗑️ Delete Sweet", use_container_width=True):
                if delete_id:
                    try:
                        service.delete_sweet(delete_id)
                        st.success(f"✅ Sweet deleted successfully!")
                        st.rerun()
                    except ValueError as e:
                        st.error(f"🚫 {str(e)}")
            st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.info("No sweets available to delete. Add some first! 🍫")
    
    st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown(
    '<div style="text-align: center; color: #6c757d; padding: 1rem;">Made with ❤️ for sweet management</div>', 
    unsafe_allow_html=True
)