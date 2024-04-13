def pickToDict(args,pickList):
    pickDict = {}
    for pickEl in pickList:
        item = args.get(pickEl)
        if item:
            pickDict[pickEl] = item
    return pickDict

# get paginated info 
def getPaginationTupple(pageQuery):
    page = int(pageQuery.get("page")) or 1
    per_page = int(pageQuery.get("per_page")) or 10
    count = True
    sort_order = pageQuery.get('sort_order') or "desc"
    sort_by =  pageQuery.get('sort_by') or "createdAt"
    return page, per_page, count, sort_order, sort_by # return tupple