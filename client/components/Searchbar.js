import { useRouter } from "next/router";

const Searchbar = ({ searchText, setSearchText }) => {
  const router = useRouter();

  const handleSubmit = (e) => {
    e.preventDefault();
    router.push(`/profile/search/${searchText}`);
  };

  return (
    <div className="flex w-full justify-center mt-8">
      <div className="flex w-full bg-white p-4 shadow rounded-full">
        <svg
          xmlns="http://www.w3.org/2000/svg"
          className="h-6 w-6"
          fill="none"
          viewBox="0 0 24 24"
          stroke="currentColor"
        >
          <path
            strokeLinecap="round"
            strokeLinejoin="round"
            strokeWidth={2}
            d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"
          />
        </svg>
        <form onSubmit={handleSubmit}>
          <input
            className="w-full pl-2 focus:outline-none"
            type="text"
            onChange={(e) => setSearchText(e.target.value)}
            value={searchText}
            placeholder="Enter name of author (i.e Tom Doherty)"
          />
        </form>
      </div>
    </div>
  );
};

export default Searchbar;
