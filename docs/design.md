# Design Document

## Components

1. Generating URLs

   * Identifying list resource weblinks
   * Webscraping and collecting links to documents
   * Save the links to text file
     ```plantuml
             @startuml
             actor Researcher as R

             R -> WebScraper: Initiate web scraping process
             WebScraper -> WebServer: Send request for web page content
             WebServer --> WebScraper: Return web page content (HTML)
             WebScraper -> WebScraper: Parse HTML to find PDF/document links
             WebScraper -> TextFile: Write links to a text file
             TextFile --> WebScraper: Confirm links saved

             R -> WebScraper: Verify completion of scraping
             WebScraper --> R: Provide status and link count

             @enduml
     ```
1. Downloading latest documents

   * Loading the links from text file
   * Downloading documents from servers if new
     ```plantuml
            @startuml
            actor Researcher as R

            R -> DocumentDownloader: Initiate document download process
            DocumentDownloader -> TextFile: Read list of links from text file
            TextFile --> DocumentDownloader: Provide list of links
            DocumentDownloader -> WebServer: Request document from link (one by one)
            WebServer --> DocumentDownloader: Return document (PDF or file)
            DocumentDownloader -> LocalStorage: Check if document is already downloaded
            LocalStorage --> DocumentDownloader: Provide document version information
            DocumentDownloader -> DocumentDownloader: Compare versions (new vs old)
            alt If new version or different document
                DocumentDownloader -> LocalStorage: Download and save the document
                LocalStorage --> DocumentDownloader: Confirm document saved
            else If no update
                DocumentDownloader -> DocumentDownloader: Skip downloading
            end

            R -> DocumentDownloader: Verify completion of download
            DocumentDownloader --> R: Provide status and download summary

            @enduml
     ```

1. Extracting and storing vectorDB

   * Parsing documents for latest information on tenders
   * Updating latest information to VectorDB
1. Quering DB using LLM

   * Querying DB with user defined query
   * Parsing results
   * Generating reports
1. Automatic updating VectorDB

   * Automate the process
   * Downloading documents to storing into VectorDB
