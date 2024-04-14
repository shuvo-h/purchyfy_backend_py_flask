def pickToDict(args,pickList):
    pickDict = {}
    for pickEl in pickList:
        item = args.get(pickEl)
        if item:
            pickDict[pickEl] = item
    return pickDict

# get paginated info 
def getPaginationTupple(pageQuery):
    page = int(pageQuery.get("page","1"))
    per_page = int(pageQuery.get("per_page","10"))
    count = True
    sort_order = pageQuery.get('sort_order', "desc")
    sort_by =  pageQuery.get('sort_by',"createdAt") 
    return page, per_page, count, sort_order, sort_by # return tupple


# QueryBuilder helpers 
# listOfFieldValues, rest = dictToPositionalList(queryDict={},fieldsToBeList=["maxPrice","minPrice"])
def dictToPositionalList(dictToBeExtracted={},fieldsToBeListed=[]):
    listOfFieldValues = [dictToBeExtracted.get(fieldName) for fieldName in fieldsToBeListed]
    restFields = {k:v for k,v in dictToBeExtracted.items() if k not in fieldsToBeListed}
    
    return listOfFieldValues, restFields 



def to_meta_dict(paginationQuery,sort_order=None,sort_by=None):
    return {
        'total_count': paginationQuery.total,
        'total_pages': paginationQuery.pages,
        'current_page': paginationQuery.page, 
        'per_page': paginationQuery.per_page,
        'has_prev': paginationQuery.has_prev,
        'has_next': paginationQuery.has_next,
        'sort_by': sort_by,
        'sort_order': sort_order
    }