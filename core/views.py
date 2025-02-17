from django.http import HttpResponse
from django.shortcuts import render


def error_404(request, exception):
    return render(request, 'core/404.html', status=404)


def robots_txt(request):
    protocol = request.scheme
    host = request.get_host()
    sitemap_url = f"{protocol}://{host}/sitemap.xml"

    lines = [
        "User-agent: *",
        "Allow: /",
        "Disallow: /admin/",
        f"Sitemap: {sitemap_url}",
    ]

    return HttpResponse("\n".join(lines), content_type="text/plain")
