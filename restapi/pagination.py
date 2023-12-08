from rest_framework.pagination import PageNumberPagination

class ContactPagination(PageNumberPagination):
   #number of objects per page 
    page_size = 100
    #перекладывается во вторую переменную, потому что нужен стринг
    page_size_query_param = 'page_size'
    max_page_size = 100
   
    page_query_param = 'p'
    last_page_strings = ['end']
