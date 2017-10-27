import medias
import fresh_tomatoes

matrix = medias.Movie("Matrix", "This is one of my favorite movie of all time. The Matrix is a science fiction action media franchise created by The Wachowskis, about heroes who fight a desperate war against machine overlords",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/c/c1/The_Matrix_Poster.jpg/220px-The_Matrix_Poster.jpg",
                        "https://www.youtube.com/watch?v=NEuZgK669zY")
print(matrix.storyline)
#matrix.show_trailer()

avatar = medias.Movie("Avatar", "A marine on an alien plannet",
                      "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                      "https://www.youtube.com/watch?v=5PSNL1qE6VY")
print(avatar.storyline)
#avatar.show_trailer()

aliens = medias.Movie("Alien","1979 science-fiction horror film ","https://images-na.ssl-images-amazon.com/images/M/MV5BNDNhN2IxZWItNGEwYS00ZDNhLThiM2UtODU3NWJlZjBkYjQxXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UY268_CR0,0,182,268_AL_.jpg",
                      "https://www.youtube.com/watch?v=bEVY_lonKf4")
print(aliens.storyline)

Lord_of_the_ring = medias.Movie("Lord of the Ring", "A ring that has extroarinary power",
                                "https://upload.wikimedia.org/wikipedia/en/8/87/Ringstrilogyposter.jpg",
                                "https://www.youtube.com/watch?v=WIrRJ8bCZYQ")
#Lord_of_the_ring.show_trailer()
print(Lord_of_the_ring.storyline)

The_hobbit = medias.Movie("The_hobbit","fantasy adventure films ","https://upload.wikimedia.org/wikipedia/en/a/a9/The_Hobbit_trilogy_dvd_cover.jpg",
                      "https://www.youtube.com/watch?v=JTSoD4BBCJc")
print(The_hobbit.storyline)

movies = [matrix, avatar, aliens, Lord_of_the_ring, The_hobbit]
fresh_tomatoes.open_movies_page(movies)
