

from . import _OnPrem


class _Network(_OnPrem):
    _type = "network"
    _icon_dir = "resource_images/onprem/network"


class Ambassador(_Network):
    _icon = "ambassador.png"


class Apache(_Network):
    _icon = "apache.png"


class Bind9(_Network):
    _icon = "bind-9.png"


class Caddy(_Network):
    _icon = "caddy.png"


class Consul(_Network):
    _icon = "consul.png"


class Envoy(_Network):
    _icon = "envoy.png"


class Etcd(_Network):
    _icon = "etcd.png"


class Glassfish(_Network):
    _icon = "glassfish.png"


class Gunicorn(_Network):
    _icon = "gunicorn.png"


class Haproxy(_Network):
    _icon = "haproxy.png"


class Internet(_Network):
    _icon = "internet.png"


class Istio(_Network):
    _icon = "istio.png"


class Jbossas(_Network):
    _icon = "jbossas.png"


class Jetty(_Network):
    _icon = "jetty.png"


class Kong(_Network):
    _icon = "kong.png"


class Linkerd(_Network):
    _icon = "linkerd.png"


class Nginx(_Network):
    _icon = "nginx.png"


class Ocelot(_Network):
    _icon = "ocelot.png"


class OpenServiceMesh(_Network):
    _icon = "open-service-mesh.png"


class Opnsense(_Network):
    _icon = "opnsense.png"


class Pfsense(_Network):
    _icon = "pfsense.png"


class Pomerium(_Network):
    _icon = "pomerium.png"


class Powerdns(_Network):
    _icon = "powerdns.png"


class Tomcat(_Network):
    _icon = "tomcat.png"


class Traefik(_Network):
    _icon = "traefik.png"


class Vyos(_Network):
    _icon = "vyos.png"


class Wildfly(_Network):
    _icon = "wildfly.png"


class Zookeeper(_Network):
    _icon = "zookeeper.png"


# Aliases

ETCD = Etcd
HAProxy = Haproxy
OSM = OpenServiceMesh
OPNSense = Opnsense
PFSense = Pfsense
VyOS = Vyos
