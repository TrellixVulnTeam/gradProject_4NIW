import ProfileList from "../../../../components/ProfileList";
import Searchbar from "../../../../components/Searchbar";

const profileSearch = ({ profiles }) => {
  return (
    <div className="w-3/4">
      <Searchbar />
      <ProfileList profiles={profiles} />
    </div>
  );
};

export async function getServerSideProps(context) {
  const res = await fetch(
    `http://localhost:5000/profile/search/${context.query.name}`
  );

  const profiles = await res.json();

  return {
    props: {
      profiles,
    },
  };
}

export default profileSearch;
