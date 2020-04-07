# Usuarios mejor valorados en Stackoverflow <img align="center" width="100" height="100" src="image/Imagen1.png"> 

## Contexto

En este proyecto se ha decidido investigar sobre Satckoverflow, un sitio web utilizado por una comunidad de desarrolladores informáticos, en la cual otros desarralladores pueden encontrar soluciones a problemas de programación de diferentes lenguajes.

Esta web pretende ser (y lo consigue) una valios ayuda para todo aquel que este encallado en alguna parte de su código de programación, fomentando la correcta formulación de las dudas y al igual que la adecuación de sus respuestas. Así de simple es su funcionamiento, pues básicamente las tres acciones más importantes en esta plataforma son preguntar, contestar y editar. 

Estas acciones son las que permiten ganar reputación (o perderla) y serán valoradas por los demás por medio de sus votos. Así que cuanto más reputación se dispongas mayor confianza generás a la comunidad. De esta manera y por medio de los votos es como se forma el liderazgo en el sitio y la razón de ser de las ligas de reputación.

De estos rankings podriamos obtener lideres de opinión y referentes que puedan impulsar proyectos open-source.

En este proyecto, accederemos al top 50 de usuarios con más reputación de lo que va de año 2020, y  extraremos información de diferentes caracteristicas y métricas.

## Descripción

Como se refiere el título, el dataset esta basado en la información más importante a para la evaluación de un usario. En este dataset se presenta los datos más relevantes para cada uno de los usuarios pertenecientes al top 50 en reputación de esta año en curso 2020. Los datos han sido entraidos en su formato natural, por lo tanto los conceptos númericos (que son enteros) los encontrará en ese formato sin signo decimal ni signo de millares, de esta manera, se podrá cargar el dataset en el software preferido y trabajar de inmediato si así se desea.

## Contenido

El dataset consta de 50 observaciones y 16 atributos atributos:

- **user:** Nombre de usuario.
- **href:** Link del usuario.
- **gold_badges:** Número de medallas de oro (durante toda la actividad).. Se obtienen al alcanzar una puntuación total de 1000 en, por lo menos, 200 respuestas.
- **silver_badges:** Número de medallas de plata (durante toda la actividad).. Se obtienen al alcanzar una puntuación total de 400 en, por lo menos, 80 respuestas.
- **bronze_badges:** Número de medallas de bronce (durante toda la actividad).. Se obtienen al alcanzar una puntuación total de 100 en por lo menos, 20 respuestas.
- **current_position:** Posición actual en el ranking anual.
- **change_position:** Variación en el ranking respecto al año anterior.
- **total_reputation:** Reputación obtenida (durante toda la actividad).
- **year_reputation:** Reputación obtenida en el año en curso.
- **answers:** Total respuestas facilitadas (durante toda su actividad).
- **questions:** Total de preguntas planteadas (durante toda su actividad).
- **people_reached:** Valor aproximado de personas alcanzadas en sus aportaciones (durante toda su actividad).
- **total_tags:** Número etiquetas en las que ha participado (durante toda su actividad).
- **top_tag:** Temática en la que más ha participado (durante toda su actividad).
- **score_top_tag:** Puntuación acumulada en la temática que más ha participado (durante toda su actividad).
- **posts_top_tag:** Número de posts de la temática que más ha participado (durante toda su actividad).
- **pct_posts_top_tag:** Porcentage sobre el total, que representa el número posts de la tématica que más ha participado (durante toda su actividad).
