<!-- Improved compatibility of back to top link: See: https://github.com/LnxRls/RmvElemsUsingMnMdDiff/pull/73 -->
<a name="readme-top"></a>
<!--
*** This is an MD README Template.
-->


<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT  -->
![Alt text](https://github.com/LnxRls/RmvElemsUsingMnMdDiff/blob/main/images/logo.png)
<br />
<div align="center">

  <h3 align="center">Data Element Removal Process</h3>

  <p align="center">
    
    <br />
    <a href="https://github.com/othneildrew/Best-README-Template"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/othneildrew/Best-README-Template">View Demo</a>
    ·
    <a href="https://github.com/othneildrew/Best-README-Template/issues">Report Bug</a>
    ·
    <a href="https://github.com/othneildrew/Best-README-Template/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        ``` <li><a href="#installation">Installation</a></li> ```
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://example.com)

This short project is based on the simple idea to remove data elements (not only outliers) from a vector of real numbers, one at a time, based on the re-calculated absolute difference of median and mean values in order to reduce any unnecessary skewness from the results, for the sake of more accurate further statistical study per analyst's judgment.    

Here's why:
* Sometimes we deal with numbers that don't necessarily stem from a process that follows a specific distribution, so the definition and removal of outliers is arbitrary and not based to the box-whisker concept    
* Detect whether there's a threshold beyond which the abs(diff(mean, median)) would either fluctuate about some value or it'll keep on dropping until the vector is left only with its last 2 elements 

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

VS Code version: 1.74.3 on Python 3.11.5

* [![Python][Python-shield]][Python-url]
* ![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

This body of code should run as is.  

### Prerequisites

The Python package prerequisites are pip, os, importlib 
  ```
  import pip, os, importlib
  ```

```
### Installation

_Below is an example of how to instruct the audience how to install and set up the code. This template doesn't rely on any external dependencies or services._

1. Get a free API Key at [https://example.com](https://example.com)
2. Clone the repo
   ```sh
   git clone https://github.com/your_username_here/Project-Name.git
   ```
3. Install NPM packages
   ```sh
   npm install
   ```
4. Enter your API in `config.js`
   ```js
   const API_KEY = 'ENTER YOUR API';
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>
```


<!-- USAGE EXAMPLES -->
## Usage

We present screenshots of 3 runs. The top pair of graphs had a threshold of 5 and the bottom 2 pairs a threshold of 0. 

![alt text](/images/RandomRun1.png "Graphs with Threshold = 5")

<p align="right">(<a href="#readme-top">back to top</a>)</p>


```
<!-- ROADMAP -->
## Roadmap

- [x] Add Changelog
- [x] Add back to top links
- [ ] Add Additional Templates w/ Examples
- [ ] Add "components" document to easily copy & paste sections of the readme
- [ ] Multi-language Support
    - [ ] Chinese
    - [ ] Spanish
```

See the [open issues](https://github.com/othneildrew/Best-README-Template/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

<!-- Your Name Here - [@your_twitter](https://twitter.com/your_username) - email@example.com -->

Project Link: [https://github.com/LnxRls/RmvElemsUsingMnMdDiff](https://github.com/LnxRls/RmvElemsUsingMnMdDiff)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

A list of helpful resources they deserve credit. 

* [Learn Python](https://www.learnpython.org/)
* [LinkedIn Advanced Python](https://www.linkedin.com/learning/advanced-python-language-features/introduction?u=218272418)
* [Python Docs](https://docs.python.org/3/)
* [Markdown Guide](https://www.markdownguide.org/basic-syntax/#reference-style-links)
<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/LnxRls/RmvElemsUsingMnMdDiff.svg?style=for-the-badge
[contributors-url]: https://github.com/LnxRls/RmvElemsUsingMnMdDiff/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/LnxRls/RmvElemsUsingMnMdDiff.svg?style=for-the-badge
[forks-url]: https://github.com/LnxRls/RmvElemsUsingMnMdDiff/network/members
[stars-shield]: https://img.shields.io/github/stars/LnxRls/RmvElemsUsingMnMdDiff.svg?style=for-the-badge
[stars-url]: https://github.com/LnxRls/RmvElemsUsingMnMdDiff/stargazers
[issues-shield]: https://img.shields.io/github/issues/LnxRls/RmvElemsUsingMnMdDiff.svg?style=for-the-badge
[issues-url]: https://github.com/LnxRls/RmvElemsUsingMnMdDiff/issues
[license-shield]: https://img.shields.io/github/license/LnxRls/RmvElemsUsingMnMdDiff.svg?style=for-the-badge
[license-url]: https://github.com/LnxRls/RmvElemsUsingMnMdDiff/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/LnxRls
[product-screenshot]: images/screenshot.png
[Python-shield]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[Python-url]: https://www.python.org/
