from fastapi import HTTPException

def get_or_404(collection:dict,id:int)->dict:
    item=collection.get(id)
    if item is None:
        raise HTTPException(
            status_code=404,
            detail=f"item with  {id} not found"
        )
    return item
collection={
    1:{"name":"Anu"},
    2:{"name":"Adhi"}
}
print(get_or_404(collection,1))
try:
    
    get_or_404(collection,3)
except HTTPException as e:
    print(e.status_code,e.detail)
       

    