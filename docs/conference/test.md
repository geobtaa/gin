<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="utf-8" />
  <!-- Give the page a title -->
  <title>BTAA Map Gallery</title>

  <meta name='viewport' content='initial-scale=1,maximum-scale=1,user-scalable=no' />
  <!-- Add a link to normalize.css -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/normalize/8.0.1/normalize.min.css" />
  <!-- Add fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Libre+Franklin&display=swap" rel="stylesheet"> 
  <!-- All the CSS code goes inside the style tags below -->
  <style>
    body {
      background: #f5f5f5;
      font-family: 'Libre Franklin', sans-serif;
      font-weight: normal;
      font-style: normal; 
      text-decoration: none;
    }

    header {
      width: 100%;
      min-width: 800px;
      margin: 0 auto;
      background: #184c7c;
      padding: 15px 0 20px;
      display: flex;
      justify-content: space-between;
      /* Push h1 and h2 to the left and right edges */
      align-items: center;
      /* Vertically center content */
      flex-wrap: wrap;
      /* Allow items to wrap to the next line if needed */
    }

    .header-elements {
      width: 80%;
      margin: 0 auto;
      display: flex;
      justify-content: space-between; /* Distribute elements horizontally */
      align-items: center; /* Vertically center content */
    }

    h1 {
      font-family: 'Libre Franklin', sans-serif;
      /*width: 80%;*/
      margin: 0 auto;
      color: whitesmoke;
      font-weight: normal;
      font-style: normal; 
      text-decoration: none;
    }

    /* Ensure that the h2 is left-aligned to the same margin as h1 */
    h2 {
      font-family: 'Libre Franklin', sans-serif;
      /*width: 80%;*/
      margin: 0 auto;
      color: whitesmoke;
      font-weight: normal;
      font-style: normal; 
      text-decoration: none;
    }

    h3 {
      font-family: 'Libre Franklin', sans-serif;
      color: #375671;
      font-weight: normal;
      font-style: normal; 
      text-decoration: none;
    }

    h4 {
      font-family: 'Libre Franklin', sans-serif;
      font-size: 1em;
      color: #375671;
      font-weight: normal;
      font-style: normal; 
      text-decoration: none;
    }

    h5 {
      font-family: 'Libre Franklin', sans-serif;
      font-size: 1.5em;
      color: #375671;
      width: 80%;
      margin: 0 auto;
      margin-top: 50px;
      margin-bottom: 25px;
      text-align: center;
      font-weight: normal;
      font-style: normal; 
      text-decoration: none;
    }

    p {
      font-size: .9em;
      color: #375671;
      /* ensure this is left-aligned to the right of the project-image */
      margin-left: 412px;
    }

    li {
      list-style-type: none;
      font-size: .9em;
      color: #375671;
      line-height: 1.6em;
      /* ensure this is left-aligned to the right of the project-image */
      margin-left: 412px;
    }

    a,
    a:visited {
      color: #003d71;
    }

    .project {
      width: 80%;
      min-width: 800px;
      height: 100%;
      margin: 35px auto;
    }

    .project:after {
      content: "";
      display: table;
      clear: both;
    }

    .project-image {
      width: 388px;
      height: 240px;
      background: white;
      float: left;
      margin-right: 20px;
      border: 2px solid #dddddd;
      object-fit: cover;
    }

    /* Adjust the dropdown styles */
    .dropdown {
      /*width: 80%;*/
      margin: 0 auto;
      margin-top: 10px;
    }

    label {
      margin: 0;
      padding: 0;
      font-family: 'Libre Franklin', sans-serif;
      color: whitesmoke;
      font-size: 16px;
      text-align: right;
      margin-right: 10px;
      font-weight: normal;
      font-style: normal; 
      text-decoration: none;
    }

    select {
      width: 70px;
      padding: 2px;
      height: auto;
      margin-right: 0px;
    }

    .gin-span {
      padding: 16px 12px;
      text-decoration: none;
      font-family: 'Libre Franklin', sans-serif;
      color: whitesmoke;
      font-size: 15px;
      font-weight: normal;
      font-style: normal; 
      text-decoration: none;
    }

    header .logo {
      display: flex;
      align-items: center;
      margin-right: 12px;
    }

    header .logo img {
      height: 60px; /* Adjust the height as needed */
      max-width: 100%; /* Make sure the image doesn't exceed its container */
    }

    .gin-link {
      text-decoration: none; /* Remove underline */
    }

    hr { 
      background-color: #375671; 
      border: none; 
      height: 1px;
      width: 5%; 
      text-align: center; 
      margin-bottom: 25px;
    } 

  </style>
</head>

<body>
  <header>
    <div class="header-elements">
      <div id="title">
        <h1>Map Gallery</h1>
        <h2>BTAA GIN Conference, <span id="year-text">2023</span></h2>
        <div class="dropdown">
          <label for="year">Select Map Gallery Year:</label>
          <select id="year">
            <!-- Make the default value the most recent year -->
            <option value="2023" selected>2023</option>
            <option value="2022">2022</option>
            <option value="2021">2021</option>
            <option value="2020">2020</option>
          </select>
        </div>
      </div>
      <div class="logo">
        <a class="gin-link" href="https://sites.google.com/umn.edu/btaa-gdp/home" aria-hidden="false" tabindex="0">
          <div class="logo">
            <img src="logo/btaa-logo-white.png" role="img" />
            <span class="gin-span">BTAA-GIN</span>
          </div>
        </a>
      </div>
    </div>
  </header>  
  <h5>Interactive Maps</h5>
  <hr>
  <div id="interactive"></div>
  <h5>Static Maps</h5>
  <hr>
  <div id="static"></div>
  <!-- Papaparse for bringing in Google spreadsheet data -->
  <script src="https://cdnjs.cloudflare.com/ajax/libs/PapaParse/5.3.0/papaparse.min.js "></script>
  <!-- Add a link to the jQuery JavaScript library so you can leverage ajax methods to load your data -->
  <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
  <!-- Custom JavaScript below -->

  <script>
    
    function loadGoogleSheetData(year) {

      // The undefined Google Sheet URL
      let gsheet;

      if (year == 2023) {
        // Define the Google Sheet URL
        gsheet = 'https://docs.google.com/spreadsheets/d/11ZhYLgbkF63YaD8cR4LcBoFzbo21PzrtBZo0DvmH2rI/export?format=csv&id=11ZhYLgbkF63YaD8cR4LcBoFzbo21PzrtBZo0DvmH2rI&gid=2060485035';
      } else if (year == 2022) {
        // Define the Google Sheet URL
        gsheet = 'https://docs.google.com/spreadsheets/d/1bOozMAKPf0nmgq2yk705u2qNV3bvHevo9S1_7YAxyTA/export?format=csv&id=1bOozMAKPf0nmgq2yk705u2qNV3bvHevo9S1_7YAxyTA&gid=1122313144';
      } else if (year == 2021) {
        // Define the Google Sheet URL
        gsheet = 'https://docs.google.com/spreadsheets/d/1rvCekjI3xqJhp0ov5NRXptzqJj_9QqaekUY0KWXp5oI/export?format=csv&id=1rvCekjI3xqJhp0ov5NRXptzqJj_9QqaekUY0KWXp5oI&gid=443168613';
      } else if (year == 2020) {
        // Define the Google Sheet URL
        gsheet = 'https://docs.google.com/spreadsheets/d/1pgUQ8ro99zt-xoNDRTA5pLhowZj-uqJRFx0dFpvtRQM/export?format=csv&id=1pgUQ8ro99zt-xoNDRTA5pLhowZj-uqJRFx0dFpvtRQM';
      };

      // Clear the interactive and static divs
      $('#interactive').empty();
      $('#static').empty();

      Papa.parse(gsheet, {
        download: true,
        header: true,
        complete: function (results) {
          // Define data
          let data = results.data;

          // Flag to track if "Static Maps" has been added
          let staticMapsAdded = false;

          // Loop through data
          for (let i = 0; i < data.length; i++) {
            // Define variables
            let project = data[i];
            let projectImage = project.image;
            let projectTitle = project.title;
            let projectAuthor = project.name + ', ' + project.affiliation + ', ' + project.institution;
            let otherAuthors = project.other_authors;

            // if there are other authors, add them to the author string
            if (otherAuthors) {
              projectAuthor = projectAuthor + ', ' + otherAuthors;
            };
            let projectDescription = project.abstract;
            let projectLink = project.link;

            // If the project is an interactive map, add it to the page
            if (project.kind.includes('Interactive Map')) {
              // Create HTML elements
              let projectHTML = '<section class="project"><a target="_blank" href="' + projectLink + '"><img src="' + projectImage + '" alt="' + projectTitle + '" class="project-image" loading="lazy" /></a><h3>' + projectTitle + '</h3><h4>' + projectAuthor + '</h4><p>' + projectDescription + '</p><li>See the map: <a target="_blank" href="' + projectLink + '">' + projectTitle + '</a></li></section>';
              // Append HTML elements to interactive div
              $('#interactive').append(projectHTML);
            };

            // If the project is a static map, add it to the page
            if (project.kind.includes('Static')) {
              // Create HTML elements
              let projectHTML = '<section class="project"><a target="_blank" href="' + projectLink + '"><img src="' + projectImage + '" alt="' + projectTitle + '" class="project-image" loading="lazy"/></a><h3>' + projectTitle + '</h3><h4>' + projectAuthor + '</h4><p>' + projectDescription + '</p><li>See the map: <a target="_blank" href="' + projectLink + '">' + projectTitle + '</a></li></section>';
              // Append HTML elements to static div
              $('#static').append(projectHTML);
            };

          };

        }
      });
    };

    // Call the function to load data for the most recent year when the page loads
    $(document).ready(function () {
      // Set the default year to the most recent year in the dropdown
      $('#year').val(2023);
      loadGoogleSheetData(2023);
    });

    // Add an event listener to the <select> element for future changes
    let selectElement = document.getElementById("year");
    selectElement.addEventListener("change", function () {
      // Get the selected year value
      const selectedYear = parseInt($(this).val());

      // Update the year-text span's text content
      $('#year-text').text(selectedYear);

      // Call the function to load data for the selected year
      loadGoogleSheetData(selectedYear);
    });
    
  </script>

</body>