# Hash
* https://golang.org/pkg/hash/
* https://softwareengineering.stackexchange.com/questions/49550/which-hashing-algorithm-is-best-for-uniqueness-and-speed
* md4, sha256 are too long

## FNV - string to number
* https://golang.org/pkg/hash/fnv/#New64
* can convert number to string using hex
```go
import (
	"fmt"
	"hash/fnv"
)

// https://gist.github.com/lenage/e8161cdfc461bf968f8687bbeae51dee
func fingerprint(b []byte) uint64 {
	hash := fnv.New64()
	hash.Write(b)
	return hash.Sum64()
}

// https://stackoverflow.com/questions/13582519/how-to-generate-hash-number-of-a-string-in-go
func hash(s string) uint32 {
        h := fnv.New32a()
        h.Write([]byte(s))
        return h.Sum32()
}

func hash(s string) string {
        h := fnv.New64()
        h.Write([]byte(s))
        return fmt.Sprintf("%x", h.Sum64())
}
```
