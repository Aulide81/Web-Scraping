<div class="fluid-row" id="header">
<h1 class="title toc-ignore">Mineria de dades: PEC3 Classificació arbres de decissió</h1>
<h4 class="author"><em>Autor: Emilio Arenas</em></h4>
<h4 class="date"><em>Noviembre 2018</em></h4>
</div>

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

Los datos fueron recopilados por medio de web scraping en Python sobre las páginas individuales de cada usuario disponibles en la web stackoverflow, pero en primer lugar se extrajo del ranking los 50 usuarios mejor valorados, que se encuentra disponible [aquí](https://stackexchange.com/leagues). Por medio de web scraping, conseguimos el nombre de usuario, link de su perfil, entre otras. Después, en disposición de estos links, se accede a cada una de las páginas individuales donde se encuentra el resto de información relevante y que es obtenida por más web scraping. Por último, los datos se almacenan en fichero CSV.

## Inspiración

El interés de analizar este conjunto de datos reside en el auge actual en las tecnólogias de software libre y los proyectos open-source. Plataformas como Stackoverflow son utilziadas periodicamente para extraer información de las tendencias actuales en lo que lenguajes de promación se refiere (ej: indice Tiobe) y guían a muchos a escoger el proximo lenguaje en aprender.

Esta set de datos además de mostrar quienes son los usuarios mejor valorados de la plataforma, también muestran en que temas parecen estar más especializados y a cuanta gente alcanza.

## Agradecimientos

El propietario del sitio web, y por lo tanto, del conjunto de datos es Stack Exchange.com, una red de webs que facilita las estadísticas de los usuarios analizados. Podemos contactar con la organización por medio de su página [web](https://stackoverflow.com/contact?referrer=https://stackoverflow.com/company/compensation/calculator).

En la página web, la organización expresa que esta en contra del scraping, así que se preferio contactar contactar con la organización para obtener su consentimiento. Para obtener el visto bueno de la organización, nos comprometimos a que no fuera una experiencia aislada y no una acción recurrente.

## Licencia

Una posible licencia para este conjunto de datos podría ser  CC BY-SA 4.0 License. La elección se basa en la ideoneidad de las clasulas que en ella se presentan en relación con el trabajo realizado donde:

- Se prohibe el nombre del creador del conjunto de datos generado y se indican los cambios realizados sobre estos. De esta manera, se reconoce el trabajo de terceros y en que medida se van realizando aportaciones en lo que se refiere al trabajo original.

- Se permite el uso comercial, lo que incrementa las posibilidades que empresas puedan interesarse en los datos generados, permitiendo así, la realización de nuevos proyectos que reporten un reconocimiento al autor original.

- Las nuevas contribuciones han de ser publicades bajo la misma licencia, lo que permite que se le reconozca al autor original en todo momento y bajo los mismo terminos que fueron planteadas para el.
