resource "linode_lke_cluster" "My-Cluster" {
    label       = "My-Cluster"
    k8s_version = "1.26"
    region      = "us-central"
    tags        = ["prod"]

    pool {
        type  = "g6-standard-2"
        count = 2
    }
}
