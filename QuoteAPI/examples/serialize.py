from author import  Author
from schema import AuthorSchema

author = Author(123, "Alex", "alex5@mail.ru")

author_schema = AuthorSchema()
# instance(экземпляр) -> dict
result = author_schema.dump(author)

print(type(result), result)

authors = [
   Author("1", "Alex"),
   Author("1", "Ivan"),
   Author("1", "Tom")
]

# Variant 1 
authors_schema = AuthorSchema(many=True)
result_one = authors_schema.dump(authors)
print(repr(result_one), type(result_one))

# Variant 2
result_two = author_schema.dump(authors, many=True)
print(repr(result_two), type(result_two))