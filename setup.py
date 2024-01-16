from setuptools import setup, find_packages


project_name = "movie_recommendation_system"

setup(
    name = project_name,
    version = "0.0.0",
    author = "Ankit M Zanzmera",
    author_email = "22msrds052@jainuniversity.ac.in",
    url = "https://github.com/Ankitzanzmera/movie_recommendation_system",
    packages = find_packages(where = "src"),
    package_dir = {"":"src"}
)