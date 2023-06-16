# Multi-Request-Repeater Burp-Suite Extender (Expanding the Scope of Penetration Testing for Automation Scanners)

## Limitations of Automation Scanners

We assume that the user knows how to set up the HCLApp scan for security testing of particular applications or targets using different types of configurations. The market offers a range of security scanners, including HCLApp scan, Acunetix, and Netsparker, among others. However, it is observed that these types of automated scanners have some disadvantages, basically, these automated security scanners are not smart enough to understand the requirements of user input fields. sometimes they are not able to reach each and every function while spidering or crawling the applications. Because of these disadvantages, it is possible that we might have missed the vulnerabilities.

Actually, we can resolve these problems by exploring the entire application manually in automation scanners.

Suppose if we want to scan a single application with multiple tools then, we have to explore the entire application multiple times for each tool.

## Purpose 
Our goal is to explore the entire application once manually and capture the traffic in the burp-suite and then transfer that captured traffic from the burp-suite to HCLApp scan or other proxy tools. However, if we want to upstream hundreds or thousands of requests, we cannot repeat each request manually in the burp-suite. In order to facilitate the upstreaming of requests, Burp Extender is developed in Jython language. This extender allows for the repetition or re-execution of multiple requests with a single click.



