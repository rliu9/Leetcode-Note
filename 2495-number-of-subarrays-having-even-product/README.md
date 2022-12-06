<h2><a href="https://leetcode.com/problems/number-of-subarrays-having-even-product/">2495. Number of Subarrays Having Even Product</a></h2><h3>Medium</h3><hr><div><p>Given a <strong>0-indexed</strong> integer array <code>nums</code>, return <em>the number of <span data-keyword="subarray-nonempty">subarrays</span> of </em><code>nums</code><em> having an even product</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> nums = [9,6,7,13]
<strong>Output:</strong> 6
<strong>Explanation:</strong> There are 6 subarrays with an even product:
- nums[0..1] = 9 * 6 = 54.
- nums[0..2] = 9 * 6 * 7 = 378.
- nums[0..3] = 9 * 6 * 7 * 13 = 4914.
- nums[1..1] = 6.
- nums[1..2] = 6 * 7 = 42.
- nums[1..3] = 6 * 7 * 13 = 546.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> nums = [7,3,5]
<strong>Output:</strong> 0
<strong>Explanation:</strong> There are no subarrays with an even product.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>5</sup></code></li>
</ul>
</div>