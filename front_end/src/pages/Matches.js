import { useState, useEffect } from 'react';
import Layout from '../Components/layout/Layout';
import MatchInfoList from '../Components/meetups/MatcchInfoList'

function MatchesPage() {
  const [isLoading, setIsLoading] = useState(true);
  const [loadedMeetups, setLoadedMeetups] = useState([]);

  useEffect(() => {
    setIsLoading(true);
    fetch(
      'http://localhost:8000/api/users'
    )
      .then((response) => {
        return response.json();
      })
      .then((data) => {
        const meetups = [];

        for (const key in data) {
          const meetup = {
            id: key,
            ...data[key]
          };

          meetups.push(meetup);
        }

        setIsLoading(false);
        setLoadedMeetups(meetups);
      });
  }, []);

  if (isLoading) {
    return (
      <Layout>
        <section>
          <p>Loading...</p>
        </section>
      </Layout>
    );
  }
  return (
    <Layout>
      <section>
        <h1>Matches</h1>
        <MatchInfoList meetups={loadedMeetups} />
      </section>
    </Layout>
  );
}

export default MatchesPage;