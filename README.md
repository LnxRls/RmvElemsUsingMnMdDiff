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


<!-- PROJECT -->

<!-- <br /> -->
<!-- <div align="center"> -->
<!--  <a href="#about-the-project">About The Project</a> -->
<!-- </div> -->


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
      </ul>
    </li>
    <li><a href="#results">Results</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

### *Iterative Data Refinement for Robust Statistical Analysis*  
This project introduces a systematic method for refining a vector of real numbers by iteratively removing data elements, not necessarily limited to conventional outliers, to minimize skewness and enhance the reliability of subsequent statistical analysis. The approach is based on dynamically recalculating the absolute difference between the median and mean after each removal, thereby progressively reducing excessive influence from disruptive data points. The decision to apply this method is subject to the analyst's judgement, and depends on the dataset’s characteristics and analytical objectives.

### *Motivation*  
Many real-world datasets do not adhere to well-defined probability distributions, making traditional outlier-detection methods (e.g., box-whisker plots, Z-scores) arbitrary or ineffective.

By examining how the absolute difference between the mean and median evolves with sequential data removal, we can empirically determine an optimal threshold for refining the dataset.

### *Key Analytical Insights*  
The iterative elimination process helps identify whether the dataset exhibits one of the following behaviors:

* Case 1 (Convergence to Minimal Elements): The absolute difference between mean and median monotonically decreases until only two elements remain  
* Case 2 (Stabilization around a Threshold): The difference fluctuates around a near-constant value despite continued removals, suggesting residual structure in the data  
* Case 3 (Hybrid Behavior): A combination of Cases 1 and 2, where an initial decline is followed by stabilization, indicating a transition in data structure  

This method provides a data-driven alternative to conventional outlier removal, particularly useful in non-parametric or distribution-agnostic settings.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

VS Code version: 1.74.3 on Python 3.11.5

* [![Python][Python-shield]][Python-url]
* ![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

This body of code should run as is, no installation is required.  

### Prerequisites

The Python package prerequisites are pip, os, importlib 
  ```
  import pip, os, importlib
  ```

<!-- RESULTS EXAMPLES -->
## Results

We present screenshots of 3 runs. The top pair of graphs had a threshold of 5 and the bottom 2 pairs a threshold of 0. The pronounced red and green hexagons in the mean vs median plot show the first and last absolute differences during execution. 

${
  \color{red} -\ Case\ 1
}$

![alt text](/images/RandomRun1.png "Graphs with Threshold = 5")

${
  \color{red} -\ Case\ 2
}$

![alt text](/images/RandomRun2.png "Graphs with Threshold = 0")

${
  \color{red} -\ Case\ 3
}$

![alt text](/images/RandomRun3.png "Graphs with Threshold = 0")
<p align="right">(<a href="#readme-top">back to top</a>)</p>


See the [open issues](https://github.com/LnxRls/RmvElemsUsingMnMdDiff/issues) for a full list of proposed features (and known issues).

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

Github Project Link: [https://github.com/LnxRls/RmvElemsUsingMnMdDiff](https://github.com/LnxRls/RmvElemsUsingMnMdDiff)

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
