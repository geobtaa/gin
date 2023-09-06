---
date: 2023-01-23
slug: 2023-01-umn-institution-blog-post-jan-2023
tags:
- legacy-blogger
title: Geospatial Data Curation Toolkit
---

# Geospatial Data Curation Toolkit

:fontawesome-solid-user: By Melinda Kernik 

Have you ever saved data in a new file format and then later realized that it no longer looks right? This is a common problem for geospatial data! If you work with geodatabases but sometimes share data in alternate file formats, this post is especially for you. <!-- more --> Geodatabases are popular among GIS researchers, but there are a limited number of software in which they can be opened. Because of this, it is a common practice to convert feature classes into shapefiles when archiving or sharing data. Shapefiles have substantial limitations, however, which can lead to loss of data and functionality during file conversion. You may have come across the truncation (and frustration) that can result from the 10 character limit on field names. There are many other limitations shapefiles have that are more difficult to notice, including limitations on the length of text fields and lack of support for time within date fields. It is easy to unintentionally alter a dataset while trying to make it accessible to a broader audience! 

![Geodatabases are able to include time within date fields, while shapefiles can only represent day, month, and year. ](https://lh6.googleusercontent.com/XDZIbztq6k6fCrBhb48uUq6InTSCz4sljvE0B1qCCVXokFRxQct8ZrzAgNqiQ6mjj6M7yjY9V_N7hcVuPgCJz55XNIXi4jC7Suz4t3ILa7t5fTg90j4VlmTCT2Dmm6xClOhyzMfZHWtOqZutjUtCK3RLiH8SqaZIIjt5IfEJp2WqqkZb_kuB8Iz20FxOXQ) Caption: The tables in this figure show what can happen if you convert a date field from a geodatabase into a shapefile.\

In the example, hours, minutes, and seconds have been removed from the shapefile version of the date field. Also, the field name in the geodatabase ("date_sampling_test") has been truncated to 10 characters ("date_sampl") in the shapefile version. The [Geospatial Data Curation Toolkit](https://github.com/mkernik/geodct) helps with this and other challenges that arise when archiving data. The `GeodatabasetoShapefileWarnings` tool generates a report describing what will be lost when converting data layers between geodatabase and shapefile formats. The toolkit also includes tools to:

* create an inventory of the data layers and fields in geodatabases
* check for missing file extensions and whether all shapefiles in a folder use the same projection 

 [The toolkit is available on GitHub](https://github.com/mkernik/geodct)! You can download the files by clicking on the green "Code" button and choosing "Download Zip." You will also find instructions about how to run the tools, a more detailed description of what they do, and sample reports. Feel free to use, share, and make derivatives! 
 
 The toolkit described in this post was developed by University of Minnesota BTAA Project Team member Melinda Kernik during a professional development leave in January 2022.
 
!!! note

	This was originally posted on blogger [here](https://geobtaa.blogspot.com/2023/01/umn-institution-blog-post-jan-2023.html).

