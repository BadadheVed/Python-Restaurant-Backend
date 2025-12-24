from fastapi import APIRouter,Body,Query
# Import the `restaurant` submodule and alias it to `restaurant_controller`
from controllers import orders as orders_controller
from uuid import UUID

router = APIRouter(
    prefix = "/orders",
    tags=["orders"]
)


@router.post("/add/{id}")
def createOrder(id: UUID, name: str = Body(..., embed=True)):
    order =  orders_controller.createOrder(id, name)
    return order


@router.get("/restaurant/{id}")
def getOrderByRestaurantId(id: UUID, page: int = 1, size: int = 10) -> list:
    orders = orders_controller.getOrdersByRestaurantId(id, page, size)
    return {
        "orders": orders,
        "total": len(orders)
    }

@router.get("/{id}")
def getById(id:UUID):
    return  orders_controller.getById(id)




