using System;
using System.Net.Http;
using System.Text;
using System.Threading.Tasks;

namespace APIClientDemo
{
    class Program
    {
        static async Task Main(string[] args)
        {
            // Your API endpoint
            string url = "http://localhost:5000/generate-prompt";

            // Dummy JSON data
            string json = @"
            {
                ""team"": ""Manchester City"",
                ""players"": [
                    {
                        ""name"": ""Player 1"",
                        ""position"": ""Goalkeeper"",
                        ""coordinates"": {""x"": 5, ""y"": 50}
                    },
                    {
                        ""name"": ""Player 2"",
                        ""position"": ""Defender"",
                        ""coordinates"": {""x"": 20, ""y"": 30}
                    }
                    // Add more players as needed
                ]
            }";

            // Create an HttpClient instance
            HttpClient client = new HttpClient();

            // Set up the request content
            HttpContent content = new StringContent(json, Encoding.UTF8, "application/json");

            try
            {
                // Make the POST request
                HttpResponseMessage response = await client.PostAsync(url, content);

                // Ensure we received a successful response
                response.EnsureSuccessStatusCode();

                // Read and output the response body
                string responseBody = await response.Content.ReadAsStringAsync();
                Console.WriteLine(responseBody);
            }
            catch (HttpRequestException e)
            {
                Console.WriteLine($"\nException Caught!");
                Console.WriteLine($"Message: {e.Message}");
            }
        }
    }
}
