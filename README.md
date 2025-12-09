# Задания 9 и 10 коллоквиума

## Задание 10

 <pre>
class User:
  users = {}
  def __init__(self, name, age=0, tags=None):
    self.name = name
    self.age = age
    self.tags = tags if tags is not None else []

  def add_tag(self, tag):
    self.tags.append(tag)

  @classmethod
  def create(cls, name, age):
    if name in cls.users:
      raise ValueError("User already exists")
    user = cls(name, age)
    cls.users[name] = user
    return user

  @classmethod
  def get(cls, name):
    return cls.users[name]

  def __str__(self):
    return f"User: {self.name} ({str(self.age)})"

u1 = User.create("Alex", 20)
u1.add_tag("admin")
print(User.get("Alex"))
print(u1)

try:
    u2 = User.create("Alex", 30)
    print(User.get("Alex"))
    print(u2)
except ValueError as e:
    print(f"Error: {e}")
</pre>
