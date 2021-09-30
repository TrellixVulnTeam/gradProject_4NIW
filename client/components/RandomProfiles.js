const RandomProfiles = ({ randomProfiles }) => {
  return (
    <div className="w-1/2">
      <div className="bg-red-200">
        <h2>Discover Publications</h2>
      </div>
      <div className="bg-green-200">
        <ul>
          {randomProfiles.map((profile) => (
            <li>{profile.name}</li>
          ))}
        </ul>
      </div>
    </div>
  );
};

export default RandomProfiles;
