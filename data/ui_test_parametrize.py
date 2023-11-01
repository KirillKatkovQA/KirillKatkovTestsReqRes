endpoints_data = [
    ("//li[@data-id='users']", "/api/users?page=2", "200"),
    ("(//a[normalize-space()='Single user'])[1]", "/api/users/2", "200"),
    ("//li[@data-id='users-single-not-found']", "/api/users/23", "404"),
    ("//a[normalize-space()='List <resource>']", "/api/unknown", "200"),
    ("(//a[normalize-space()='Single <resource>'])[1]", "/api/unknown/2", "200"),
    ("//a[normalize-space()='Single <resource> not found']", "/api/unknown/23", "404"),
    ("//a[normalize-space()='Create']", "/api/users", "201"),
    ("(//a[@data-key='try-link'][normalize-space()='Update'])[1]", "/api/users/2", "200"),
    ("(//a[@data-key='try-link'][normalize-space()='Update'])[2]", "/api/users/2", "200"),
    ("//a[normalize-space()='Delete']", "/api/users/2", "204"),
    ("//a[normalize-space()='Register - successful']", "/api/register", "200"),
    ("//a[normalize-space()='Register - unsuccessful']", "/api/register", "400"),
    ("//a[normalize-space()='Login - successful']", "/api/login", "200"),
    ("//a[normalize-space()='Login - unsuccessful']", "/api/login", "400"),
    ("//a[normalize-space()='Delayed response']", "/api/users?delay=3", "200")
]
