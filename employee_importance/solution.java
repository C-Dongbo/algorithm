class Employee {
    // It's the unique id of each node;
    // unique id of this employee
    public int id;
    // the importance value of this employee
    public int importance;
    // the id of direct subordinates
    public List<Integer> subordinates;
};

class Solution {
    
	int result = 0;
	Map<Integer, Employee> employeeMap = new HashMap<>();
	
	public int getImportance(List<Employee> employees, int id) {
		for(Employee e : employees) {
			employeeMap.put(e.id, e);
		}
		return dfs(id);
	}
	
	public int dfs(int id) {
		result = employeeMap.get(id).importance;
		for(int subId : employeeMap.get(id).subordinates) {
			result += dfs(subId);
		}
		return result;
	}
}
