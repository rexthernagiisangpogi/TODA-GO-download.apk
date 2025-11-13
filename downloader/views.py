from django.shortcuts import render

def home(request):
    app_info = {
        'name': 'TODA GO',
        'version': '1.0.0',
        'description': 'The fastest way to get a ride. Track, book, and ride with trusted tricycle drivers — all in one tap.',
        'features': [
            'Easy to use interface with intuitive design',
            'Lightning fast performance and optimization',
            'Cross-platform compatibility (Windows, Mac, Linux)',
            'Regular updates and security patches',
            'Free lifetime support and documentation',
        ],
        'download_url': 'https://github.com/rexthernagiisangpogi/TODA-GO/releases/download/TODA_GO/Toda_Go.apk',
        'file_size': '15.2 MB',
        'requirements': {
            'os': 'Windows 10/11, macOS 10.15+, or Linux',
            'ram': '2GB RAM minimum, 4GB recommended',
            'storage': '100MB free disk space',
            'internet': 'Internet connection for installation'
        }
    }
    return render(request, 'downloader/home.html', {'app': app_info})
