### HOSxP Doctor Queue restart

```markdown
# IP Loader and HTTP GET Example

This Python script demonstrates how to load a list of IP addresses from a file (`ips.txt`) and send HTTP GET requests to each IP address.

## Requirements

- Python 3.x
- `requests` library (install via `pip install requests`)

## Usage

1. Clone this repository:
   ```bash
   git clone https://github.com/your-repo-name/ip-loader.git
   cd ip-loader
   ```

2. Install the required `requests` library:
   ```bash
   pip install requests
   ```

3. Prepare your IP list file `ips.txt` with one IP address per line.

4. Run the script:
   ```bash
   python ip_loader.py
   ```
1
   This will iterate through each IP address listed in `ips.txt`, send a GET request to `http://<ip_address>`, and print the response status code.

## Example `ips.txt` content

```
129.0.6.101
129.0.6.102
129.0.6.106
129.0.6.107
129.0.6.108
129.0.6.109
129.0.6.111
129.0.6.115
129.0.6.116
129.0.6.119
129.0.6.201
129.0.6.203
129.0.6.205
```

Each IP address in the file should be on a separate line.

## Notes

- Make sure the IP addresses in `ips.txt` are accessible and respond to HTTP GET requests.
- Handle any potential errors related to network connectivity or server responses in your own applications.


**Super Thank**: ChatGPT