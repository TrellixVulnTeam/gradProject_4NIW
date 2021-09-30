import Pagination from "../../../../components/Pagination";
import ProfileList from "../../../../components/ProfileList";
import Searchbar from "../../../../components/Searchbar";

const profile = ({ profiles, currentPage, prevPage, nextPage, lastPage }) => {
  return (
    <div className="w-3/4 flex-col">
      <Searchbar />
      <ProfileList profiles={profiles} />
      <Pagination
        currentPage={currentPage}
        prevPage={prevPage}
        nextPage={nextPage}
        lastPage={lastPage}
      />
    </div>
  );
};

export async function getServerSideProps(context) {
  const res = await fetch(
    `http://localhost:5000/profile/page/${context.query.page}`
  );

  const profiles = await res.json();

  const lastPage = profiles.pop();
  const nextPage = profiles.pop();
  const prevPage = profiles.pop();

  return {
    props: {
      profiles: profiles,
      currentPage: context.params.page,
      prevPage: prevPage,
      nextPage: nextPage,
      lastPage: lastPage,
    },
  };
}

export default profile;
