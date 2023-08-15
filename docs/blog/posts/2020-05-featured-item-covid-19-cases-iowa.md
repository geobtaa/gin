---
date: '2020-05-04'
slug: 2020-05-featured-item-covid-19-cases-iowa
tags:
- legacy-blogger
title: 'Featured Item: Covid-19 Cases: Iowa'
---

# Featured Item: Covid-19 Cases: Iowa

By Jay Bowen

## Covid-19 Cases: Iowa > > > > 

[![Example of GeoJSON URL screen](https://blogger.googleusercontent.com/img/a/AVvXsEiE8BWuaB4eH46uPUJ0nNze0bz_Wl6TLDOy0EYJIKmNvAX8icNpLRuQqzeYH783USC7d0xL1J8gZjNftUgX9EGQvORluPRZs9lyFUJqShxwwxXgMUkICllP7CH5CVs5f7KMKvVQUomzP-sX2Xql0vwAxM0hG97-eNsxGs2M5Q1dhnxm-SWLVn9vt_xjZQ=w200-h173)](https://blogger.googleusercontent.com/img/a/AVvXsEiE8BWuaB4eH46uPUJ0nNze0bz_Wl6TLDOy0EYJIKmNvAX8icNpLRuQqzeYH783USC7d0xL1J8gZjNftUgX9EGQvORluPRZs9lyFUJqShxwwxXgMUkICllP7CH5CVs5f7KMKvVQUomzP-sX2Xql0vwAxM0hG97-eNsxGs2M5Q1dhnxm-SWLVn9vt_xjZQ){ width="300" }

 As concerns over the global coronavirus pandemic have intensified, Iowans may be wondering if there is a reliable geospatial dataset that they can access to do their own monitoring of the virus in Iowa. Through the BTAA Geoportal, the public can freely access the Covid-19 Cases: Iowa dataset, which is hosted by Iowa Open Spatial Data and updated and maintained by the Iowa Department of Public Health. Through this dataset, you can download a shapefile displaying the total confirmed cases and deaths due to <!-- more --> COVID-19 by county. Of particular interest to those who wish to make a more than static map of the outbreak in Iowa are the API options offered. Here, you can simply copy the GeoJSON URL and plug it into the JavaScript supporting your online map, allowing your map to display automatically the updated GeoJSON. 

[![Map of Confirmed cases Polk County, Iowa](https://blogger.googleusercontent.com/img/a/AVvXsEhE58f2pN150UJQ8ZkkGdIAjnVqGhlri2UmFZB0zHsJKKBe_hcnsfOH1xZRnM0e6jEsLa3PX60ejfi3izs1hlxT8jF8YYBozsfIB-3LVvR8ukjo1KHPtypja9G0ssOZh1fSkfZYJPaMalbIraVlu0c6WIOR50nwu8RJmB6ZyMmJ26xVYje1H929b5C92g=w400-h309)](https://blogger.googleusercontent.com/img/a/AVvXsEhE58f2pN150UJQ8ZkkGdIAjnVqGhlri2UmFZB0zHsJKKBe_hcnsfOH1xZRnM0e6jEsLa3PX60ejfi3izs1hlxT8jF8YYBozsfIB-3LVvR8ukjo1KHPtypja9G0ssOZh1fSkfZYJPaMalbIraVlu0c6WIOR50nwu8RJmB6ZyMmJ26xVYje1H929b5C92g){ width="300" }

 What I like about this option is that it gives you constant access to the most recent data published by the Iowa Department of Public Health. If you modify your scripting to dynamically classify and color code your data, as well as to style your legend, you can build a map that will self-update appropriately as long as the dataset continues to be revised. I have chosen to classify my data by 5 ck-means clusters using the [Simple Statistics](https://simplestatistics.org/F&sa=D&sntz=1&usg=AOvVaw1Xl8NdYil-TRZL-pcUn4JZ) JavaScript library. I also used [ColorBrewer](https://colorbrewer2.org/F&sa=D&sntz=1&usg=AOvVaw0hbEbaYMpBCSZRMnKSWvsg) to select an appropriate color scale for these five classes. I went with a single-hue 5-class blue set of colors for my map. I also included popup content so that users can access the up-to-date case and death count for each county when they click on a county polygon. This popup also displays how recently the data were updated. By clicking an information button in the top-right corner, users can find more information about the map and the data included. In the top-right corner, there is also a layer control, so that you can toggle between cases and deaths by county. Users can also use the zoom control to display the map at their preferred scale. If you would like to see the data and code behind this [map](https://ui-libraries.github.io/FIowa_COVID19_Map/F&sa=D&sntz=1&usg=AOvVaw0HRnG68tgQIrNpvV8iEsQ-), you can take a look at the GitHub repository [here](https://github.com/Fui-libraries/FIowa_COVID19_Map&sa=D&sntz=1&usg=AOvVaw29f_VErvvqakjoYk0qdJVf).

### What BTAA Library submitted the item? University of Iowa ### Interesting tidbits:
 * Contains updated county-level data on COVID-19 cases and deaths for the State of Iowa
 * Allows API options for using GeoJSON data in online mapping instead of requiring downloads 

[![Map of The Covid-19 Cases: Iowa dataset in the BTAA Geoportal](https://blogger.googleusercontent.com/img/a/AVvXsEji-Ib1LwO25jfZO14t7eZeb0ZgJkd3DmPM74HY8METihTFeWW3h6HPM8UMsNKBkGpfrNt_p3HUc_5c26hABp8vemhxYriz9_ricWqTtjPaXT5rSq1q8zJ0HMyI7Wj7L-8ltKzC5amjXdecS_XI4D9DviN-8339s0YYbhfcTm1FhZf6VQbL1IBB4ktxYA=w640-h362)](https://geo.btaa.org/catalog/6a84756c2e444a87828bb7ce699fdac6_0){ width="300" }

 --- [The Covid-19 Cases: Iowa dataset in the BTAA Geoportal](https://geo.btaa.org/catalog/6a84756c2e444a87828bb7ce699fdac6_0)

### Where can I find out more? [](https://www.lib.uiowa.edu&sa=D&sntz=1&usg=AOvVaw1dEVyooHA-6TI-e3PxWiFJ) [](https://www.lib.uiowa.edu&sa=D&sntz=1&usg=AOvVaw1dEVyooHA-6TI-e3PxWiFJ)
 * [](https://www.lib.uiowa.edu&sa=D&sntz=1&usg=AOvVaw1dEVyooHA-6TI-e3PxWiFJ)[University of Iowa Libraries](https://www.lib.uiowa.edu&sa=D&sntz=1&usg=AOvVaw1dEVyooHA-6TI-e3PxWiFJ)
 * [Digital Scholarship & Publishing Studio, University of Iowa](https://www.lib.uiowa.edu/studio/) [](https://sites.google.com/umn.edu/btaa-gdp/news/2020/05/04-iowa_covid19?authuser=0#h.p_2x9a6PWUlG8r)Have questions about this item, the BTAA geoportal, or maps and geospatial data in general? Please don’t hesitate to [contact our project team](https://geo.btaa.org/feedback)! _Jay Bowen is the GIS Specialist at the Digital Scholarship & Publishing Studio, University of Iowa Libraries. _*This was originally posted on blogger [here](https://geobtaa.blogspot.com/2020/05/featured-item-covid-19-cases-iowa.html)*.

