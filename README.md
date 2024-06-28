# Duck Generator
The purpose of this program is to draw images of ducks (specifically PDs) at a regular interval.

## Running Locally

### Prerequisites

1. Install [podman](https://podman.io/) or [docker](https://www.docker.com/) if not installed already.

1. Clone the repository and navigate into the project's root directory.

### Steps to Run
*Note: if using docker simply replace `podman` with `docker` on the commands.*

1. Build the image from the Containerfile:</br>
`podman build -t duck-generator .`

1. Create a container from the image:</br>
`podman run -d --name duck-generator-container duck-generator:latest`

## Useful Commands
*Note: if using docker simply replace `podman` with `docker` on the commands.*

#### List all ducks stored:
`podman exec -it duck-generator-container tree /ducks`

#### List all ducks stored for a specific day:
`podman exec -it duck-generator-container tree /ducks/2024-06-28`

#### Copy ducks into local working directory for viewing:
`podman cp duck-generator-container:/ducks .`
