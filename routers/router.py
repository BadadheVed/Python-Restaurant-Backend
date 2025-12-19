from fastapi import APIRouter,Body,Query
# Import the `restaurant` submodule and alias it to `restaurant_controller`
from controllers import restaurant as restaurant_controller
from uuid import UUID
router = APIRouter(
    prefix="/restaurants",
    tags=["restaurants"],
)

@router.get("/")
def get_all_restaurants(page:int = Query("page", ge=1), size:int = Query("size", ge=1, le=100)):
    return restaurant_controller.getAll(page, size)
@router.post("/add")
def addRestaurant(name: str = Body(..., embed=True)):
    return restaurant_controller.addRestaurant(name)

@router.get("/{id}")
def getById(id:UUID):
    return restaurant_controller.getRestaurantById(id)