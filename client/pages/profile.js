import ProfileList from "../components/ProfileList";

const profile = ({ profiles }) => {
  return (
    <>
      <h2>profiles are here</h2>
      <ProfileList profiles={profiles} />
    </>
  );
};

export default profile;

export async function getStaticProps(context) {
  //  const res = await fetch(`https://jsonplaceholder.typicode.com/posts?_limit=6`)
  const res = await fetch(`http://localhost:5000/profile/page/2`);
  const profiles = await res.json();

  return {
    props: {
      profiles,
    },
  };
}
