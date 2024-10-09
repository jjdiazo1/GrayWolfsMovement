# GreyWolfPathAnalysis

The **GreyWolfPathAnalysis** project focuses on the analysis of grey wolf movement patterns in the Alberta region of Canada. Using GPS telemetry data and various data structures such as graphs, hash tables, and stacks, this project seeks to answer key questions about wolf migration corridors, territorial behavior, and the effects of environmental conditions. The project integrates concepts from previous data structures such as Lists, Stacks, Queues, Maps, and Ordered Maps.

This repository is part of the **Data Structures and Algorithms (EDA)** teaching framework at Universidad de los Andes. The repository was developed by faculty professors and staff in the Department of Systems and Computer Engineering (DISC) and uses the Non-Object-Oriented Python library **DISCLib**.

[DISClib][disclib-url] · [DISClib Demo and Examples][demo-url] · [Report Bug][challenge4-bugs-url] · [Request Feature][challenge4-issues-url]

## Members

The students edit this section to add their names, Uniandes emails, and specify which project functionality of the project they will implement.

1. Student No. 1 Ángel Farfán, Student No. 1 Uniandes Email a.farfana@uniandes.edu.co, Student No. 1 20222183.
1. Student No. 2 Juan José Díaz, Student No. 2 Uniandes Email jj.diazo1@uniandes.edu.co, Student No. 2 202220657.
1. Student No. 3 Name Andrés Cáceres, Student No. 3 Uniandes Email a.caceresg@uniandes.edu.co, Student No. 3 202214863.

[Back to top](#greywolfpathanalysis)

## About The Project

This project provides tools to analyze the movement patterns of grey wolves in the Alberta region of Canada. By leveraging directed and undirected graphs, the project helps visualize migration paths, identify common meeting points, and assess the effects of environmental conditions on wolf behavior. It integrates data structures like hash tables, stacks, and trees to efficiently manage large datasets from GPS telemetry records, offering insights into wolf territories and corridors under various climatic conditions.

**IMPORTANT** This is a work in progress and is part of a teaching framework for undergraduate college students at Universidad de los Andes. This project Is NOT intended as a full-functional source code project.

## Structure

The challenge template has four main parts:

1. [DISClib](./DISClib) Root folder with the official course library. For more on its implementation, visit the [DISClib Repository][disclib-url].
2. [App](./App) Folder with the model-view-controller (MVC) Python scripts. In here, the students implement their code to complete the challenge.
3. [Data](./Data) Folder with CSV data files to load into the application. Students must add the course-provided data files to complete the challenge.
4. [Docs](./Docs) Folder with reports, data tables, and other documentation. Students add their project report, data tables, and other documentation to complement their code implementation.

[Back to top](#greywolfpathanalysis)

## Requirements

### Requirement 1: Plan a possible route between two meeting points (Group)

As a conservationist biologist, I want to know if there is a path between two meeting points used by wolves. The expected output includes:

- Total distance between the two points.
- Total number of meeting points along the path.
- Total number of tracking nodes (wolf movements) in the path.
- First and last five vertices (including the origin and destination) with:
  - Identifier of the meeting point.
  - Latitude and longitude of the point.
  - Number of wolves present at the point.
  - First and last wolf identifiers that transit through that point.

### Requirement 2: Plan a route with the fewest stops between two meeting points (Group)

As a conservationist biologist, I want to know the corridor with the fewest points (meeting or tracking) between an origin and destination point. The expected output includes:

- Total distance between the two points.
- Total number of meeting points along the path.
- Total number of tracking nodes in the path.
- First and last five vertices (including the origin and destination) with:
  - Identifier of the meeting point.
  - Latitude and longitude of the point.
  - Number of wolves present at the point.
  - First and last wolf identifiers that transit through that point.

### Requirement 3: Identify territories inhabited by different packs (Individual)

As a park ranger, I want to know the territories of wolf packs within the forest habitat. The output must contain:

- Total number of packs identified by their meeting and tracking points.
- The top five packs with the most control over territory, including:
  - Number of meeting and tracking points within the territory.
  - First and last three meeting points in the territory.
  - Number of wolves in the pack.
  - First and last three members of the pack, including:
    - Wolf identifier.
    - Taxonomy.
    - Life stage.
    - Sex.
    - Study location.
  - Maximum and minimum latitude and longitude of the territory.

### Requirement 4: Identify the shortest path between two points in the habitat (Individual)

As a park ranger, I want to identify the shortest migration corridor between two specific points within the Athabasca Oil Sands Region (AOSR). The expected output includes:

- Distance between the origin GPS point and the nearest meeting point.
- Distance between the destination GPS point and the nearest meeting point.
- Total distance of the path between origin and destination.
- Total number of meeting points along the path.
- Total number of wolves using the identified corridor.
- First and last three meeting points (including the origin and destination) with:
  - Identifier of the meeting point.
  - Latitude and longitude.
  - Number of wolves present at the point.
  - First and last wolf identifiers that transit through that point.

### Requirement 5: Identify the longest migration corridor (Individual)

As a park ranger, I want to recognize the longest migration corridor I can inspect from a specific meeting point. The output must include:

- Maximum number of possible routes for inspection.
- The longest migration corridor, with:
  - Number of visited meeting and tracking points.
  - Total distance covered.
  - Sequence of meeting points and wolves along the route.

### Requirement 6: Identify differences in migration corridors by wolf type (Group)

As a conservationist biologist, I want to identify behavioral differences in wolves based on their sex over a given period. The expected output includes two parts:

1. The wolf that covered the most distance in the given range:
   - Wolf identifier, taxonomy, life stage, sex, and study location.
   - Total distance traveled.
   - Longest route taken by the wolf:
     - Total possible distance traveled.
     - Total number of meeting and tracking points along the path.
     - First and last three meeting points with:
       - Identifier of the meeting point.
       - Latitude and longitude.
       - Number of wolves present at the point.
       - First and last wolf identifiers.

2. The wolf that covered the least distance with similar details as above.

### Requirement 7: Identify changes in pack territories based on climatic conditions (Group)

As a conservationist biologist, I want to observe the effects of climatic conditions on pack mobility and the territory they can cover. The output must contain:

- Total number of packs identified by their movement and meeting points.
- The first and last three packs with the largest territory based on meeting points, including:
  - Number of wolves in the pack.
  - First and last three pack members, including:
    - Wolf identifier, taxonomy, life stage, sex, and study location.
  - Maximum and minimum latitude and longitude in the territory.
  - The longest route identified within the territory.

### Requirement 8: Bonus - Visualize results for all requirements (Group)

As a conservationist biologist, I want to visualize the results of all the application requirements. For this, teams are encouraged to graphically represent the results using multimedia resources and graphical interfaces. Suggested tools include the `folium` Python library for visualizing geospatial data.

[Back to top](#greywolfpathanalysis)

## Usage

To use this template, you need to follow the steps below:

* Read the official project document published in the course official site at [BrightSpace][BrightSpace-url].
* Distribute the project functionalities and implementation responsibilities among the group members.
* Download the official dataset for the project at the course official site at [BrightSpace][BrightSpace-url].
* Unzip and load the dataset into the application at the [Data](./Data) folder.
* Import the necessary modules from [DISClib](./DISClib) into the MVC scripts at the [App](./App) folder.
* Implement the missing functions according to the project needs in the MVC scripts at the [App](./App) folder.
* Evaluate the implementation of the MVC scripts, record your tests and analysis in the documents at the [Docs](./Docs) folder (The report **MUST BE** in PDF format).

[Back to top](#greywolfpathanalysis)

## Contact and support

For further information and contact, use the following links:

* Official Repository [DISClib][disclib-url].
* Repository for [Demo and Examples][demo-url].

If you require further information, please contact us [via this email](mailto:isis1225@uniandes.edu.co).

[Back to top](#greywolfpathanalysis)

## Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this project better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".

Don't forget to give the project a star! Thanks again!

1. Fork the Project.
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`).
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the Branch (`git push origin feature/AmazingFeature`).
5. Open a Pull Request.

[Back to top](#greywolfpathanalysis)

## License

Copyright 2020, Departamento de sistemas y Computación, Universidad de Los Andes.
Developed for the class _"ISIS1225 - Estructuras de Datos y Algoritmos"_ or _"ISIS1225 - Data Structure and Algorithms"_ in English.

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the [GNU General Public License](LICENSE) for more information go to [GNU ORG][gnu-url].

[Back to top](#greywolfpathanalysis)

## Authors and acknowledgment

* [Dario Correal][dariocorreal-url] is the original author and main developer of the library.
* [Santiago Arteaga][phillipus85-url] is a contributor and repository administrator. 
* [Luis Florez][le99-url] is a contributor and developed examples and tutorials for the library.

[Back to top](#greywolfpathanalysis)

<!-- MARKDOWN LINKS & IMAGES -->
[contributors-shield]: https://img.shields.io/github/contributors/ISIS1225DEVS/ISIS1225-Lib.svg?style=for-the-badge
[contributors-url]: https://github.com/ISIS1225DEVS/ISIS1225-Lib/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/ISIS1225DEVS/ISIS1225-Lib.svg?style=for-the-badge
[forks-url]: https://github.com/ISIS1225DEVS/ISIS1225-Lib/network/members
[stars-shield]: https://img.shields.io/github/stars/ISIS1225DEVS/ISIS1225-Lib.svg?style=for-the-badge
[stars-url]: https://github.com/ISIS1225DEVS/ISIS1225-Lib/stargazers
[issues-shield]: https://img.shields.io/github/issues/ISIS1225DEVS/ISIS1225-Lib.svg?style=for-the-badge
[issues-url]: https://github.com/ISIS1225DEVS/ISIS1225-Lib/issues
[license-shield]: https://img.shields.io/badge/License-GPLv3-blue.svg?style=for-the-badge
[license-url]: https://github.com/ISIS1225DEVS/ISIS1225-Lib/blob/master/LICENSE
[disclib-url]: https://github.com/ISIS1225DEVS/ISIS1225-Lib
[demo-url]: https://github.com/ISIS1225DEVS/ISIS1225-Examples
[gnu-url]: http://www.gnu.org/licenses/
