docker build -t aylinjg/my-flask-app:latest .
docker push aylinjg/my-flask-app:latest

kubectl apply -f <nombre>
k get pods 

Kubernetes:k8s, automatiza la implementacion y gestiona apps en contenedores. Es para desplegar applicaciones, gestionar ciclo de vida, etc.  Hace que funcionen todas las apps qu se tengan, que se repartan el trabajo y no se caigan 
kubectl: crea, actuaiza y elimina recursos (pods, deployments, services), te permite ver los estados del cluster, depura apps y gestiona configuraciones (Basicamente hace operaciones administrativas)
Helm Chart: gestiona los paquetes de kubernetes. Simplifica el hecho de instalar apps complejas, permite instalar cosas con un solo comando.
Registry en kubernetes: Almacena las imagenes de contenedores y luego son utilizadas por kubernetes para desplegar  apps. DockerHub es el registry publico mas conocido. Amazon Elastic Container o Azzure Container Registry tambien pero son privados. 
Manifest de kubernetes:Archivo de configuracion escrito YAML o JSON que describe los recursos que se desea crear en el cluster. 
Los recursos pueden ser:
Pods -> la unidad mas pequeña
Deployments -> Gestionan el ciclo de vida de los Pods (escalamiento, actualizaciones, etc.)
Services -> Exponen aplicaciones dentro del clúster o al exterior.
ConfigMaps y Secrets -> Almacenan configuraciones y datos sensibles.
-----------------------------------------------------------------------------------------
### Estructura de un manifest 

ejemplo de un manifest simple para un Pod 
apiVersion: v1
kind: Pod
metadata:
  name: mi-pod
spec:
  containers:
    - name: mi-contenedor
      image: nginx:latest
------------------------------------------------------------------------------------




-----------------------------------------------------------------------------------
### Estructura de un manifest de kubernetes 
tiene los siguientes campos:

-apiVersion: Especifica la versión de la API de Kubernetes que se está utilizando (por ejemplo, v1, apps/v1).

-kind: Define el tipo de recurso que se está creando (por ejemplo, Pod, Deployment, Service).

-metadata: Contiene metadatos como el nombre del recurso, etiquetas (labels) y anotaciones (annotations).

-spec: Define la configuración específica del recurso. Por ejemplo:

Para un Pod: los contenedores que se ejecutarán.
Para un Deployment: el número de réplicas y la plantilla del Pod.

-Status: (Opcional) Este campo es gestionado por Kubernetes y muestra el estado actual del recurso


apiVersion: apps/v1
kind: Deployment
metadata:
  name: mi-deployment
spec:
  replicas: 3
  selector:
    matchLabels:
      app: mi-app
  template:
    metadata:
      labels:
        app: mi-app
    spec:
      containers:
        - name: mi-contenedor
          image: nginx:latest
-----------------------------------------------------------------------------------
Cluster: Un equipo de máquinas que trabajan juntas.

AKS: Kubernetes listo para usar en Azure.

Formas de correr un Cluster: En la nube: AKS, GKE, EKS, etc.

Localmente: Minikube, Kind, k3s, Docker Desktop.

Tipos de recursos en Kubernetes: Pods, Deployments, Services, ConfigMaps, Secrets, Namespaces, Volumes, Ingress.
------------------------------------------------------------------------------------------------------------------

### 1. **¿Qué es el `values.yaml` en Helm?**
Es un archivo de configuracion donde defines los valores personalizados para tu aplicación (como nombres, contraseñas, tamaños, etc.),
 que luego Helm usa para generar los recursos de Kubernetes.

### 2. **¿Qué es una Release en Helm?**
Es una instancia instalada de un Chart en tu clúster de Kubernetes. 
Cada vez que instalas un Chart, se crea una Release única con su propia configuración.

---

### 3. **¿Qué es un Chart en Helm?**
Es un **paquete** que contiene todo lo necesario para desplegar una aplicación en Kubernetes: 
archivos YAML, plantillas y valores configurables.


- **`values.yaml`**: Archivo de configuración para personalizar tu aplicación.
- **Release**: Una instancia instalada de un Chart en Kubernetes.
- **Chart**: Un paquete con todo lo necesario para desplegar una aplicación.
