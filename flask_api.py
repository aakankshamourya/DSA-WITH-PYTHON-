"""
Flask API for DSA Solutions
"""

from flask import Flask, request, jsonify
import sys
from pathlib import Path

app = Flask(__name__)

# Helper functions from DSA solutions
def reverse_words(s):
    """Reverse words in a string"""
    return ' '.join(s.split()[::-1])

def two_sum(nums, target):
    """Find two numbers that add up to target"""
    num_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
    return []

def max_subarray_sum(nums):
    """Find maximum sum of contiguous subarray (Kadane's algorithm)"""
    if not nums:
        return 0
    max_sum = current_sum = nums[0]
    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum

def palindrome_check(s):
    """Check if string is palindrome"""
    s = s.lower().replace(" ", "")
    return s == s[::-1]

def is_sorted(arr):
    """Check if array is sorted"""
    return arr == sorted(arr)

# API Routes
@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({"status": "healthy", "message": "DSA API is running"}), 200

@app.route('/api/reverse-words', methods=['POST'])
def api_reverse_words():
    """
    Reverse words in a string
    Expected JSON: {"text": "hello world"}
    """
    try:
        data = request.get_json()
        text = data.get('text', '')
        result = reverse_words(text)
        return jsonify({"input": text, "output": result}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/api/two-sum', methods=['POST'])
def api_two_sum():
    """
    Find two numbers that sum to target
    Expected JSON: {"nums": [2, 7, 11, 15], "target": 9}
    """
    try:
        data = request.get_json()
        nums = data.get('nums', [])
        target = data.get('target', 0)
        result = two_sum(nums, target)
        return jsonify({"nums": nums, "target": target, "indices": result}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/api/max-subarray-sum', methods=['POST'])
def api_max_subarray():
    """
    Find maximum sum of contiguous subarray
    Expected JSON: {"nums": [-2, 1, -3, 4, -1, 2, 1, -5, 4]}
    """
    try:
        data = request.get_json()
        nums = data.get('nums', [])
        result = max_subarray_sum(nums)
        return jsonify({"nums": nums, "max_sum": result}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/api/palindrome-check', methods=['POST'])
def api_palindrome():
    """
    Check if string is palindrome
    Expected JSON: {"text": "racecar"}
    """
    try:
        data = request.get_json()
        text = data.get('text', '')
        result = palindrome_check(text)
        return jsonify({"input": text, "is_palindrome": result}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/api/is-sorted', methods=['POST'])
def api_is_sorted():
    """
    Check if array is sorted
    Expected JSON: {"nums": [1, 2, 3, 4, 5]}
    """
    try:
        data = request.get_json()
        nums = data.get('nums', [])
        result = is_sorted(nums)
        return jsonify({"nums": nums, "is_sorted": result}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/api/endpoints', methods=['GET'])
def list_endpoints():
    """List all available endpoints"""
    endpoints = {
        "GET /health": "Health check",
        "POST /api/reverse-words": "Reverse words in string",
        "POST /api/two-sum": "Find two numbers that sum to target",
        "POST /api/max-subarray-sum": "Find maximum sum of contiguous subarray",
        "POST /api/palindrome-check": "Check if string is palindrome",
        "POST /api/is-sorted": "Check if array is sorted",
        "GET /api/endpoints": "List all endpoints"
    }
    return jsonify(endpoints), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
