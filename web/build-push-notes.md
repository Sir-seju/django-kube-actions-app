## Login with your API Token

```
docker login
```

## Build your container image locally

```
docker build -t graystum/django-k8s-web:latest -f Dockerfile .
```

## Push your container image

```
docker push graystum/django-k8s-web --all-tags
```

Naturally, for all these steps replace `registry.digitalocean.com/cfe-k8s/` with your container registry and `django-k8s` with whatever image name you want to give your Django project.
