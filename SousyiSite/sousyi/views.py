from django.shortcuts import render
from .models import Track

def tracks_page(request):
    # Получаем все треки
    tracks = Track.objects.all().select_related(
        'album_id', 
        'genre_id'
    ).prefetch_related('artist_id')
    
    # Перевод длительности в минуты:секунды
    for track in tracks:
        track.duration_formatted = f"{track.duration // 60}:{track.duration % 60:02d}"
    
    total_tracks = tracks.count()
    
    # Кол-во уникальных исполнителей
    unique_artists = set()
    for track in tracks:
        for artist in track.artist_id.all():
            unique_artists.add(artist.name)
    
    context = {
        'tracks': tracks,
        'total_tracks': total_tracks,
        'unique_artists_count': len(unique_artists),
    }
    return render(request, 'tracks.html', context)