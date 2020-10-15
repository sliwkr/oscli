
URL_DOWNLOAD='https://www.opensubtitles.com/api/v1/download'
"""
POST
file_id  ID of the file to download
sub_format  Format (optional, default to original. possible values: srt, sub, mpl, webvtt, dfxp, txt)
file_name  Desired name of the returned file
strip_html  Remove HTML tags (default false)
cleanup_links  Remove HTML links
remove_adds  Remove ads
in_fps  Input FPS (advanced, default to original subtitle FPS)
out_fps  Output FPS
timeshift  Timeshift, (+/- time in ms or s, eg +2s or -200ms)
"""
URL_FIND='https://www.opensubtitles.com/api/v1/find'
"""
GET
id  ID of the movie or episode
imdb_id  IMDB ID of the movie or episode
tmdb_id  TMDB ID of the movie or episode
type  movie, episode or all, (default: all)
query  file name or text search
languages  Language code(s), coma separated (en,fr)
moviehash  Moviehash of the movie
user_id  To be used alone - for user uploads listing
hearing_impaired  include, exclude, only. (default: include)
foreign_parts_only  include, only (default: include)
trusted_sources  include, only (default: include)
machine_translated  exclude, include (default: exclude)
ai_translated  exclude, include (default: exclude)
order_by  Order of the returned results, accept any of above fields
order_direction  Order direction of the returned results (asc,desc)
"""
