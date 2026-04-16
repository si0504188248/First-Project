# K3s Overview

## What is it?
**K3s** is a lightweight and compact Kubernetes distribution. It is designed to be a single binary executable of less than 100MB that contains everything necessary to run a fully functional and secure Kubernetes cluster.




## When should it be used?
You should use K3s in any situation where you want the power of Kubernetes without the heavy overhead and complexity of the standard version. It is perfect for:
* **Automated Testing (CI/CD):** When you need to spin up a cluster quickly to run tests.
* **Local Development Environment:** For developers who want to run containers on their personal computers without slowing them down.
* **Small Scale Projects:** Hosting simple websites or applications.

## Where can it be used?
Due to its minimal resource consumption, K3s can be run almost anywhere:
* **IoT & Edge Devices:** Such as Raspberry Pi or industrial controllers.
* **Personal Computers:** On Windows, Mac, or Linux (especially within WSL).
* **Low-Resource Cloud Servers:** On very small and affordable virtual machines.


## Why should I use it?
* **Simplicity:** Rapid installation with just a single command.
* **Resource Efficiency:** Consumes significantly less RAM and CPU than standard Kubernetes.
* **Production Ready:** Despite its size, it is secure and suitable for real-world production environments.
* **Full Compatibility:** Every standard Kubernetes command (kubectl) works exactly the same way here.
