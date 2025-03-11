from django.shortcuts import render

def home(request):
    return render(request, 'freelancer/home.html')

def services(request):
    services_list = ["Web Development", "SEO Optimization", "Graphic Design", "Digital Marketing"]
    return render(request, 'freelancer/services.html', {'services': services_list})

def testimonials(request):
    testimonials_data = {
        "John Doe": "Great work! The website turned out perfect.",
        "Jane Smith": "Excellent communication and top-notch service.",
        "Emily Johnson": "Delivered beyond expectations, highly recommended!"
    }
    return render(request, 'freelancer/testimonials.html', {'testimonials': testimonials_data})

def pricing(request):
    pricing_data = {
        "Web Development": "$1000",
        "SEO Optimization": "$500",
        "Graphic Design": "$300",
        "Digital Marketing": "$700"
    }
    return render(request, 'freelancer/pricing.html', {'pricing': pricing_data})

def case_studies(request):
    return render(request, 'freelancer/case_studies.html')

def blog(request):
    return render(request, 'freelancer/blog.html')
