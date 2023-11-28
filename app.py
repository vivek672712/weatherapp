import streamlit as st
import requests

def main():
    st.title("KNOW YOUR CITIES WEATHER")
    page_bg_img ='''
    <style>
    [data-testid="stAppViewContainer"]{
    background-image : url(https://images.mid-day.com/images/images/2023/jun/PTI06_13_2023_000319A_33194066_d.jpg);
    background-size : cover;
    }

'''
    st.markdown(page_bg_img, unsafe_allow_html=True)
    
    


if __name__ == "__main__":
    main()

api_key = "a0bb0412deccbec6c17747badeeb20a7"

st.title("WEATHER APP")
city_name = st.text_input("ENTER CITY NAME", "india")

if st.button("Get Weather"):
    api_url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}'

    response = requests.get(api_url)
    if response.status_code == 200:
        # Parse the JSON response
        weather_data = response.json()

        # Extract relevant information
        temperature = int(weather_data['main']['temp'] -273.15)
        description = weather_data['weather'][0]['description'] 
        humidity = weather_data['main']['humidity']

        # Display the weather information
        st.write(f"Temperature: {temperature} C")
        st.write(f"Description: {description}")
        st.write(f"Humidity: {humidity}%")
    else:
        # Display an error message if the request fails
        st.write(f"Error: Unable to fetch weather data. Status Code {response.status_code}")

# Display Streamlit app
