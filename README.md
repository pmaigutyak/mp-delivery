# MP-delivery

Django delivery app.

### Installation

1) Install with pip:

```
pip install django-mp-delivery
```

2) Add app to urls.py:

```
path('delivery/', include('delivery.urls')),
```

3) Add delivery settings
```
from delivery.settings import DeliverySettings

class CommonSettings(
        ...
        DeliverySettings,
        BaseSettings):
    pass
```

4) Run `python manage.py migrate`


### Model
```
from delivery.models import DeliveryMethodField
 
delivery_method = DeliveryMethodField()
```


### Template
```
{% include 'delivery/form.html' %}
 
 
{% block js %}
    {{ block.super }}
 
    {% include 'delivery/js.html' %}
{% endblock %}
```
