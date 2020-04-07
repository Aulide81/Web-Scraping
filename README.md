<div class="fluid-row" id="header">
<h1 class="title toc-ignore">Tipología y ciclo de vida de los datos: Práctica 1</h1>
<p class="author"><em>Autor: Emilio Arenas</em></p>
</div>

# Usuarios mejor valorados en Stack overflow <img align="center" width="150" height="200" src="image/Imagen1.png"> 

## Contexto

En este proyecto se ha decidido investigar sobre Satck overflow, un sitio web utilizado por una comunidad de desarrolladores informáticos, en la cual otros desarrolladores pueden encontrar soluciones a problemas de programación de diferentes lenguajes.

Esta web pretende ser (y lo consigue) una valiosa ayuda para todo aquel que este encallado en alguna parte de su código de programación, fomentando la correcta formulación de las dudas y al igual que la adecuación de sus respuestas. Así de simple es su funcionamiento, pues básicamente las tres acciones más importantes en esta plataforma son preguntar, contestar y editar.

Estas acciones son las que permiten ganar reputación (o perderla) y serán valoradas por los demás por medio de sus votos. Así que cuanta más reputación se dispongas mayor confianza generas a la comunidad. De esta manera y por medio de los votos es como se forma el liderazgo en el sitio y la razón de ser de las ligas de reputación.

De estos rankings podríamos obtener líderes de opinión y referentes que puedan impulsar proyectos open source.

En este proyecto, accederemos al top 50 de usuarios con más reputación de lo que va de año 2020, y extraeremos información de diferentes características y métricas.


## Descripción

Como se refiere el título, el dataset está basado en la información más importante para la evaluación de un usuario. En este dataset se presenta los datos más relevantes para cada uno de los usuarios pertenecientes al top 50 en reputación de este año en curso 2020. Los datos han sido extraídos en su formato natural, por lo tanto los conceptos numéricos (que son enteros) los encontrará en ese formato sin signo decimal ni signo de millares, de esta manera, se podrá cargar el dataset en el software preferido y trabajar de inmediato si así se desea.

## Contenido

El dataset consta de 50 observaciones y 16 atributos atributos:

- **user:** Nombre de usuario.
- **href:** Link del usuario.
- **gold_badges:** Número de medallas de oro (durante toda la actividad). Se obtienen al alcanzar una puntuación total de 1000 en, por lo menos, 200 respuestas.
- **silver_badges:** Número de medallas de plata (durante toda la actividad). Se obtienen al alcanzar una puntuación total de 400 en, por lo menos, 80 respuestas.
- **bronze_badges:** Número de medallas de bronce (durante toda la actividad). Se obtienen al alcanzar una puntuación total de 100 en por lo menos, 20 respuestas.
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
- **pct_posts_top_tag:** Porcentaje sobre el total, que representa el número posts de la temática que más ha participado (durante toda su actividad).

Los datos fueron recopilados por medio de web scraping en Python sobre las páginas individuales de cada usuario disponibles en la web stack overflow, pero en primer lugar se extrajo del ranking los 50 usuarios mejor valorados, que se encuentra disponible [aquí](https://stackexchange.com/leagues). Por medio de web scraping, conseguimos el nombre de usuario, link de su perfil, entre otras. Después, en disposición de estos links, se accede a cada una de las páginas individuales donde se encuentra el resto de información relevante y que es obtenida por más web scraping. Por último, los datos se almacenan en fichero CSV.


## Inspiración

El interés de analizar este conjunto de datos reside en el auge actual en las tecnologías de software libre y los proyectos open source. Plataformas como Stack overflow son utilizadas periódicamente para extraer información de las tendencias actuales en lo que lenguajes de programación se refiere (ej.: indice Tiobe) y guían a muchos a escoger el próximo lenguaje en aprender.

Esta set de datos además de mostrar quienes son los usuarios mejor valorados de la plataforma, también muestra en que temas parecen estar más especializados y a cuanta gente alcanza.


## Agradecimientos

El propietario del sitio web, y por lo tanto, del conjunto de datos es Stack Exchange.com, una red de webs que facilita las estadísticas de los usuarios analizados. Podemos contactar con la organización por medio de su página [web](https://stackoverflow.com/contact?referrer=https://stackoverflow.com/company/compensation/calculator).

En la página web, la organización expresa que está en contra del scraping, así que se prefirió contactar con la organización para obtener su consentimiento. Para obtener el visto bueno de la organización, nos comprometimos a que no fuera una experiencia aislada y no una acción recurrente.

## Licencia

Una posible licencia para este conjunto de datos podría ser  CC BY-SA 4.0 License. La elección se basa en la idoneidad de las cláusulas que en ella se presentan en relación con el trabajo realizado donde:

- Se prohíbe el nombre del creador del conjunto de datos generado y se indican los cambios realizados sobre estos. De esta manera, se reconoce el trabajo de terceros y en qué medida se van realizando aportaciones en lo que se refiere al trabajo original.

- Se permite el uso comercial, lo que incrementa las posibilidades que empresas puedan interesarse en los datos generados, permitiendo así, la realización de nuevos proyectos que reporten un reconocimiento al autor original.

- Las nuevas contribuciones han de ser publicadas bajo la misma licencia, lo que permite que se le reconozca al autor original en todo momento y bajo los mismo términos que fueron planteadas para él.

## Código Python y dataset

Tanto el código fuente como el dataset generado se encuentran en este repositorio. Además también se ha subido el dataset a la plataforma de Zenodo.
