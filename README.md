## Fastapi microservice template

The aim of this template is
1. To facilitate the creation of microservices under the proposed structure,
2. To consolidate a structure that reflects best practices and standards.

### Usage
In order to create a new project under the structure in this template, we use
[copier](https://github.com/copier-org/copier) as a template engine.
1. In order to install **copier**, follow the installation instructions 
[here](https://github.com/copier-org/copier?tab=readme-ov-file#installation),
considering in particular that we are going to use **copier** through its CLI.
2. Create a new project with
    ```shell
    copier copy path/to/project/template path/to/destination
    ```
3. Respond to all the project parameters. These can be known beforehand 
by reading the file `copier.yml`.
