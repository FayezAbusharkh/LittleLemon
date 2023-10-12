API Endpoints for Testing:

1. Menu API:
   - GET, POST: /restaurant/menu/
   - GET, PUT, DELETE: /restaurant/menu/<id>/

2. Booking API (using viewset):
   - GET, POST, DELETE, etc.: /restaurant/bookings/
   - Details for specific booking (GET, PUT, DELETE, etc.): /restaurant/bookings/<id>/

3. Authentication:
   - Obtain Token: /api-token-auth/

4. User Registration and Authentication (using Djoser):
   - Endpoints: /auth/

Note: Replace `<id>` with the actual ID of the item when testing specific item details.

